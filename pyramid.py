import cv2
import numpy as np
img=cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)
smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)
cv2.imshow('Smaller Image',smaller)
cv2.imshow('Larger Image',larger)
cv2.waitKey(0)
cv2.destroyAllWindows()
