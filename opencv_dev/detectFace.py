'''
얼굴 인식 소스 
1. 설치 라이브러리
pip install numpy
2. 실행 
윈도우상에 실행할때 20여초 시간 걸림
'''
import numpy as np
import cv2

# Cascades 디렉토리의 haarcascade_frontalface_default.xml 파일을 Classifier로 사용
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#cap.set(3,640) # set Width 윈도우에선 굳이 필요없음
#cap.set(4,480) # set Height

while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue

    #img = cv2.flip(img, -1) # 상하반전
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('video', img) # video라는 이름으로 출력

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()