
# sudo pip3 install Adafruit_DHT

import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 4

try:
    while True:
        h, t = dht.read_retry(sensor, pin)
        if h is not None and t is not None:
            print("Temp = {0:0.1f}C Humidity = {1:0.1f}%".format(t, h))
        else:
            print("Read error")
        
        time.sleep(1) 
    print("Terminated by Keyboard")

finally:
    print("End of program")