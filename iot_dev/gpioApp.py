'''
라즈베리파이 GPIO 테스트 소스
2색 LED 점멸 테스트
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

try:
    while True:
        GPIO.output(21, False)
        GPIO.output(20, True)
        time.sleep(0.1)
        GPIO.output(20, False)
        GPIO.output(21, True)
        time.sleep(0.1)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()