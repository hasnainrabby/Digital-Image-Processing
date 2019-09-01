import cv2
import numpy as np
img =cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
height,weight=img.shape[:2]
print(height)
print(weight)
quater_height,quater_weight=height/4,weight/4
print(quater_height)
print(quater_weight)
T=np.float32([[1,0,quater_weight],[0,1,quater_height]])
print(T)
img_translation=cv2.warpAffine(img,T,(weight,height))
cv2.imshow('Original Image',img)
cv2.imshow('Translation image',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()