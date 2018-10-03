import cv2

image = cv2.imread('26.jpg', 0)
image = cv2.bitwise_not(image)
cv2.imshow("image", image)
cv2.waitKey(0)