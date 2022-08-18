import RPi.GPIO as GPIO
import pygame
import time

GPIO.setwarnings(False)
btnPin = 12; GPIO.setmode(GPIO.BCM); GPIO.setup(btnPin, GPIO.IN)
pygame.mixer.init()
critical = pygame.mixer.Sound('Critical.wav')

if __name__ == '__main__':
    try:
        while True:
            inputIO = GPIO.input(btnPin)

            if inputIO == False:
                print("OFF")
            else:
                print("ON")
                critical.play()

            time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()