import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
camera = PiCamera()
counter = 1

if __name__ == "__main__":
    while True:
        if GPIO.input(pirPin) == GPIO.HIGH:
            try:
                camera.start_preview()
                time.sleep(0.5)
                camera.capture('/home/pi/image%s.jpg' % counter)
                counter = counter + 1
            except Exception as ex:
                print('{}'.format(ex))
            finally:
                camera.stop_preview()
        time.sleep(3)