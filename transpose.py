import cv2
img= cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
rotate_image= cv2.transpose(img)
cv2.imshow('Original Image',img)
cv2.imshow('Rotated Image',rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()