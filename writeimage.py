import cv2
img =cv2.imread('C:\\Users\Aspire\Desktop\pic.jpg',0)
new_image=cv2.imwrite('C:\\Users\Aspire\Desktop\pic2.jpg',img)
print('IMAGE written to file system:',new_image)