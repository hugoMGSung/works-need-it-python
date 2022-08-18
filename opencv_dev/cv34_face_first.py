'''
얼굴 인식 최초 파이선 소스
1. 설치 라이브러리
pip install numpy
2. 실행 
윈도우상에 실행할때 20여초 시간 걸림
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cap.set(3,640) # set Width, 윈도우에서는 필요없음
#cap.set(4,480) # set Height

while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue

    #frame = cv2.flip(img, -1) # Flip camera vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('img', img)
    cv2.imshow('gray', gray)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()