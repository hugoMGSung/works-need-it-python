import smbus2
import bme280
import time

port = 1; address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

if __name__ == '__main__':
    try:
        while True:
            data = bme280.sample(bus, address)
            t = data.temperature
            h = data.humidity
            p = data.pressure
            print('"Temp = {0:0.1f}C Humid = {1:0.1f}% Pressure = {2:0.1f}'.format(t, h, p))
            time.sleep(1)
    except KeyboardInterrupt:
        print('Error')