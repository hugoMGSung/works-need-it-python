import RPi.GPIO as GPIO
import time

inaPin = 17
inbPin = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(inaPin, GPIO.OUT)
GPIO.setup(inbPin, GPIO.OUT)

GPIO.output(inaPin, GPIO.HIGH)
time.sleep(5)
GPIO.output(inaPin, GPIO.LOW)
time.sleep(5)
GPIO.output(inbPin, GPIO.HIGH)
time.sleep(5)
GPIO.output(inbPin, GPIO.LOW)
time.sleep(0.5)