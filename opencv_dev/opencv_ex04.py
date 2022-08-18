# 블러
import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (10,10)) # 10 x 10 커널 평균값으로 이미지 흐리게

cv2.imshow('Blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()