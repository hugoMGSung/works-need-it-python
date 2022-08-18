# 기본 이미지 처리
import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original', org)
cv2.imshow('Gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()