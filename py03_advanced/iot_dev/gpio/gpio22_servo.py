import RPi.GPIO as GPIO
import time

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

if __name__ == '__main__':
    time.sleep(5)
    setServoPos(0)
    time.sleep(3)
    setServoPos(45)
    time.sleep(3)
    setServoPos(90)
    time.sleep(3)
    setServoPos(90+45)
    time.sleep(3)
    setServoPos(180)
    time.sleep(3)

    m.stop()
    GPIO.cleanup()