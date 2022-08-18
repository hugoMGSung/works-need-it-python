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
                camera.start_recording('/home/pi/video%s.h264' % counter)
                counter = counter + 1
                time.sleep(7)
                
                                
            except Exception as ex:
                print('{}'.format(ex))
            finally:
                camera.stop_recording()
                camera.stop_preview()
        time.sleep(3)