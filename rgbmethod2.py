import cv2
img=cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg',0)
cv2.imshow('Gray scale image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()