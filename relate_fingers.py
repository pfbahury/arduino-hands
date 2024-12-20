import os
import cv2 as cv
import serial
import time
from cvzone.HandTrackingModule import HandDetector
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("SERIAL_PORT")

hand_detector = HandDetector(maxHands = 1)

arduinoData = serial.Serial(PORT, 9600)
time.sleep(1)
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("failed to grab frame")
        break

    hands, img = hand_detector.findHands(frame)

    if hands:
        hand = hands[0]
        fingers = hand_detector.fingersUp(hand)

        fingers_str = "".join(map(str, fingers)) + '\n'

        # print(fingers_str)
        arduinoData.write((fingers_str).encode('utf-8'))
        time.sleep(0.05)

    
    cv.imshow("frame", frame)

    if cv.waitKey(1) & (cv.getWindowProperty("frame", cv.WND_PROP_VISIBLE) < 1):
        break

cap.release()
cv.destroyAllWindows()