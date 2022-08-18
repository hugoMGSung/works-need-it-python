import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)

GPIO.output(buzzer, GPIO.HIGH)
time.sleep(3)
GPIO.output(buzzer, GPIO.LOW)
time.sleep(0.5)