# 이미지 대비 높이기
import cv2
import numpy as np

org = cv2.imread('./opencv_dev/image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

cv2.imshow('Enhance', enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()