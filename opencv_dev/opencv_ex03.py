# 이미지 자르기
import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

height, width, channel = org.shape
print(width)

img_cropped = org[:, :int(width / 2)]
cv2.imshow('Half', img_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()