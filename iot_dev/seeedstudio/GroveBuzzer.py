import time
import RPi.GPIO as GPIO
 
GPIO.setwarnings(False)
buzzer = 12; GPIO.setmode(GPIO.BCM); GPIO.setup(buzzer, GPIO.OUT)
 
while True:
    try:
        # Buzz for 1 second
        GPIO.output(buzzer, GPIO.HIGH)
        print ('start')
        time.sleep(1)
        # Stop buzzing for 1 second and repeat
        GPIO.output(buzzer, GPIO.LOW)
        print ('stop')
        time.sleep(1)
 
    except KeyboardInterrupt:
        GPIO.output(buzzer, GPIO.LOW)
        break
    except IOError:
        print ("Error")
