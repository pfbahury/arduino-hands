import cv2 as cv
import mediapipe as mp
import time
import serial

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

arduinoData = serial.Serial("com4", 9600)
time.sleep(1)

# Armazena o estado anterior dos dedos
previous_signal = "0"
send_delay = 0.5  # Tempo de espera entre envios de dados (em segundos)
last_send_time = time.time()

def finger_raised(hand_landmarks):
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

    if (index_tip < index_pip) and (middle_tip > middle_pip) and (ring_tip > ring_pip) and (pinky_tip > pinky_pip) and (thumb_tip > thumb_mcp):
        return "1"
    elif (index_tip < index_pip) and (middle_tip < middle_pip) and (ring_tip > ring_pip) and (pinky_tip > pinky_pip) and (thumb_tip > thumb_mcp):
        return "2"
    elif (index_tip < index_pip) and (middle_tip < middle_pip) and (ring_tip < ring_pip) and (pinky_tip > pinky_pip) and (thumb_tip > thumb_mcp):
        return "3"
    elif (index_tip < index_pip) and (middle_tip < middle_pip) and (ring_tip < ring_pip) and (pinky_tip < pinky_pip) and (thumb_tip > thumb_mcp):
        return "4"
    elif (index_tip < index_pip) and (middle_tip < middle_pip) and (ring_tip < ring_pip) and (pinky_tip < pinky_pip) and (thumb_tip < thumb_mcp):
        return "5"
    else:
        return "0"

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

            current_signal = finger_raised(hand_landmarks)

            # Envia os dados somente se o estado mudar ou se passar o tempo de espera
            if current_signal != previous_signal and (time.time() - last_send_time) > send_delay:
                arduinoData.write(current_signal.encode())
                previous_signal = current_signal
                last_send_time = time.time()  # Atualiza o tempo do último envio

    cv.imshow("frame", frame)

    if cv.waitKey(1) & (cv.getWindowProperty("frame", cv.WND_PROP_VISIBLE) < 1):
        break

cap.release()
cv.destroyAllWindows()
