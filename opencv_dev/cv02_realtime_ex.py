import cv2
 
cap = cv2.VideoCapture(0)   # 0: default camera
#cap = cv2.VideoCapture("test.mp4") #동영상 파일에서 읽기
 
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        # 프레임 출력
        cv2.imshow('Camera Window', frame)
 
        # ESC를 누르면 종료
        key = cv2.waitKey(1) & 0xFF
        if (key == ord('q')): break
 
cap.release()
cv2.destroyAllWindows()