# 내장 카메라로 실시간 화면 띄우기
import cv2

# 카메라 객체 선언 및 설정
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = capture.read()     # 카메라에서 현재 영상 받아 frame에 저장, 잘 받았다면 ret가 참
    cv2.imshow("video", frame)      # frame(카메라 영상)을 video이름의 창에 띄움 
    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
            break

capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()