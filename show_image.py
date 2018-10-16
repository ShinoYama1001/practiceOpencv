#coding:utf-8

import cv2

img = cv2.imread("cloud.png")
img2 = cv2.imread("image.png")

cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("im", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()