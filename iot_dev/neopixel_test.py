'''
네오픽셀 초기 테스트 파이썬 소스

1. 기본 라이브러리 ws281x, neopixel 설치
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
필요시 아래도 설치
sudo python3 -m pip install --force-reinstall adafruit-blinka
2. Red - 5V
   White - Ground
   Green - Sinal(GPIO18) 연결
3. 실행시는 반드시 콘솔에서 
   sudo python neopixel_test.py 
   로 실행할 것!!
'''

import board
import neopixel
import time

def main():
    try:
        pixel_pin = board.D18 # 보드에 GPIO 핀 설정
        num_pixels = 30 # LED칩 갯수
        # 초기화
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
        
        pixels.fill((0, 0, 0))
        time.sleep(1)
        pixels[0] = (255, 0, 0)
        time.sleep(1)
        pixels.fill((0, 255, 0))
        time.sleep(1)

        count = 0
        while count < num_pixels:
            pixels[count] = (255, 0, 0)
            count += 1
            time.sleep(0.1)

        pixels.fill((0, 0, 255))
        time.sleep(2)

    except KeyboardInterrupt:
        pass
    finally:
        pixels.deinit() # 최종 릴리즈    
    
    
if __name__ == '__main__':
    main()
