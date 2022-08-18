import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 25
scale = [262,294,330,349,392,440,494,523] # 도레미파솔라시도 주파수
#scale = [493,261] # 도레미파솔라시도 주파수
GPIO.setup(buzzer, GPIO.OUT)

p = GPIO.PWM(buzzer, 600) # 주파수 600 PWM 생성
p.start(50) # 듀티사이클 50%
try:
    while True:
        for i in range(8): # or 2
            p.ChangeFrequency(scale[i])
            time.sleep(0.5)
    
finally:
    p.stop() # PWM stop
    GPIO.cleanup()