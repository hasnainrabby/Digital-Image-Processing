import cv2
img=cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
cv2.imshow('Original image',img)
cv2.waitKey(0)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Convert image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()