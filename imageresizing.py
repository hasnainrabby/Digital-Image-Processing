import cv2
import numpy as np
img=cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)
img_scaled=cv2.resize(img,None,fx=0.75,fy=0.75)               #3/4 of our original image
cv2.imshow('Scaling Linear Interpolation',img_scaled)
cv2.waitKey(0)
img_scaled1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)  #double size of img
cv2.imshow('Scaling Cubic Interpolation',img_scaled1)
cv2.waitKey(0)
img_scaled2=cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling skewed size', img_scaled2)
cv2.waitKey(0)
cv2.destroyAllWindows()
