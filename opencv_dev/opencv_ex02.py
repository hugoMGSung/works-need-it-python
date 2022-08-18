# 사이즈 변경
import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

size_small = cv2.resize(org, (160, 80))
cv2.imshow('Small', size_small)

cv2.waitKey(0)
cv2.destroyAllWindows()