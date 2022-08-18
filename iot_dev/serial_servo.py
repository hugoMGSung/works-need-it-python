import RPi.GPIO as GPIO
import serial

port = '/dev/ttyACM0'
brate = 9600 #boudrate
cmd = 'temp'

servoPin = 12
SERVO_MAX_DUTY = 12 # 서보 최대180도 위치 주기
SERVO_MIN_DUTY = 3  # 서보 최소0도 위치 주기

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

m = GPIO.PWM(servoPin, 50)
m.start(0)

ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)

def setServoPos(degree):
    if degree > 180:
        degree = 180
    
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    print('Degree {} to {}'.format(degree, duty))
    m.ChangeDutyCycle(duty)

if __name__ == '__main__':
    while True:
        try:
            if ser.in_waiting != 0:
                content = ser.readline()
                content = content.decode('utf-8').replace('\r\n', '')
                vals = content.split(':')
                print(vals)
                if vals[0] == '0':
                    setServoPos(90)
                elif vals[0] == '1023':
                    setServoPos(180)
                if vals[1] == '0':
                    setServoPos(90)
                elif vals[1] == '1023':
                    setServoPos(0)
        except KeyboardInterrupt:
            GPIO.cleanup()
            