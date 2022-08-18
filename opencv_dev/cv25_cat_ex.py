# 선명하게
import cv2
import numpy as np

org = cv2.imread('./opencv_dev/image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])

sharp = cv2.filter2D(gray, -1, kernel)
cv2.imshow('Original', org)
cv2.imshow('Sharp', sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()