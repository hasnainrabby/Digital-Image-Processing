import cv2
img=cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg')
cv2.imshow('Original Image',img)
print(img.shape)
print('Height of the image pixel value:', img.shape[0])
print('Width of the image pixel value:', img.shape[1])
print('Layer of the image value:', img.shape[2])
cv2.waitKey(0)
cv2.destroyAllWindows()