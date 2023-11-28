import cv2
import numpy as np

image = cv2.imread('C:/Users/asus/Downloads/Task_3.jpg', 0)


# Simple thresholding
ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Task_3_simple.jpg', th1)
print(th1)

# Adaptive thresholding
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Task_3_adaptive.jpg', th2)
# print(th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
