import cv2
img = cv2.imread('1.jpg')

print 'Hello!'
cv2.imshow('bgr image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
