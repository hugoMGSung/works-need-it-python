import serial

port = '/dev/ttyACM0'
brate = 9600 #boudrate
cmd = 'temp'

ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)

while True:
    if ser.in_waiting != 0:
        content = ser.readline()
        print(content)
        # print(content[:-2].decode())
        #content = content.decode('utf-8').replace('\r\n', '')
        #vals = content.split(':')
        #print(vals)