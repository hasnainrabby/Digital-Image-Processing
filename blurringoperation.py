import cv2
import numpy as np

img = cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
cv2.imshow('Original image', img)
cv2.waitKey(0)
#Create 3x3 Kernel
Kernal_3x3=np.ones((3,3),np.float32)/9
blurred=cv2.filter2D(img,-1,Kernal_3x3)
cv2.imshow('Kernal_3x3 blurring',blurred)
cv2.waitKey(0)
#Create 7x7 Kernel
Kernal_7x7=np.ones((7,7),np.float32)/49
blurred1=cv2.filter2D(img,-1,Kernal_7x7)
cv2.imshow('Kernal_7x7 blurring',blurred1)
cv2.waitKey(0)
cv2.destroyAllWindows()
