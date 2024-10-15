import time
import serial

arduinoData = serial.Serial("com4", 9600)
time.sleep(1)

while True:
    s = input("Digite 0 ou 1: ")
    if s != "0" and s != "1":
        print("Digite 0 ou 1")
        continue
    else:
        arduinoData.write(s.encode())
        
