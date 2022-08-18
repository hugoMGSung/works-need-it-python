import RPi.GPIO as GPIO
import time

servo_pin = 23 #PWM pin 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
p = GPIO.PWM(servo_pin, 50)
p.start(0)

if __name__ == '__main__':
    try:
        while True:
            p.ChangeDutyCycle(3)
            time.sleep(5)
            p.ChangeDutyCycle(7.5)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        p.stop()
        GPIO.cleanup()