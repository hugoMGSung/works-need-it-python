import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

if __name__ == "__main__":
    while True:
        if GPIO.input(pirPin) == GPIO.HIGH:
            print("Motion detected!!")
        else:
            print("No motion")
        time.sleep(0.2)