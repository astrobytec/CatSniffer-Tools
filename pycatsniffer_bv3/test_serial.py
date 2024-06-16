import serial
import time

ser = serial.Serial()
ser.port = "/dev/tty.usbserial-10"
ser.baudrate = 115200
ser.open()
try:
    while True:
        print(ser.readline())
        time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()