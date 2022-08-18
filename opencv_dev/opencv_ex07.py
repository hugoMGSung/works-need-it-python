# 경계선 감지
import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
# 픽셀 강도의 중간값을 계산
median_intensity = np.median(gray)
# 중간 픽셀 강도에서 위아래 1 표준편차 떨어진 값을 임곗값으로 지정
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
# Canny edge detection 적용
image_canny = cv2.Canny(gray, lower_threshold, upper_threshold)
cv2.imshow('Canny', image_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()