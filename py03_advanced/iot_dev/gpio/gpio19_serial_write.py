import serial
import time

port = '/dev/ttyACM0'
brate = 9600 #boudrate
cmd = 'temp'

ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)

while True:
    ser.write(b'1')
    time.sleep(2)
    ser.write(b'2')
    time.sleep(2)
