import cv2
import numpy as np
img=cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
height,width=img.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,1)
rotated_image=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow('Original image',img)
cv2.imshow('Rotated image',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()