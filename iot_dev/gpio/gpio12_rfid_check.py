import serial
import RPi.GPIO as GPIO

port = '/dev/ttyACM0'
brate = 9600 #boudrate
search = 'RESULT'
ser = serial.Serial(port, baudrate=brate, timeout=None)

servoPin = 23
SERVO_MAX_DUTY = 12 # 서보 최대180도 위치 주기
SERVO_MIN_DUTY = 3  # 서버 최소0도 위치 주기
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
m = GPIO.PWM(servoPin, 50)
m.start(0)

def setServoPos(degree):
    if degree > 180:
        degree = 180
    
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
    print('Degree {} to {}'.format(degree, duty))
    m.ChangeDutyCycle(duty)

def procValid(isOk):
    if isOk == True:
        setServoPos(180)
        print('Opened')
    elif isOk == False:
        setServoPos(0)
        print('Not Opened')

if __name__ == '__main__':
    while True:
        if ser.in_waiting != 0:
            content = ser.readline()
            content = content[:-2].decode('utf-8')
            if search in content:
                vals = content.split(':')
                if vals[1] == 'ON':
                    procValid(True)
                else:
                    procValid(False)

    m.stop()
    GPIO.cleanup()