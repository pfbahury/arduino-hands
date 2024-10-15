import cv2 as cv
import mediapipe as mp
import time
import serial

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1)
mp_drawing = mp.solutions.drawing_utils

arduinoData = serial.Serial("com4", 9600)
time.sleep(1)

def is_hand_closed(hand_landmarks):

    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x

    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y

    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y

    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y

    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
    pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y


    if (index_tip > index_pip) and (middle_tip > middle_pip) and (ring_tip > ring_pip) and (pinky_tip > pinky_pip) and (thumb_tip > thumb_mcp):
        return True
    return False
    


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("failed to grab frame")
        break

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_hand_closed(hand_landmarks):
                arduinoData.write('0'.encode())
            else:
                arduinoData.write('1'.encode())

    cv.imshow("frame", frame)

    if cv.waitKey(1) & (cv.getWindowProperty("frame", cv.WND_PROP_VISIBLE) < 1):
        break

    
cap.release()
cv.destroyAllWindows()