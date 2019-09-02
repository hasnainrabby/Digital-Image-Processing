import cv2
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame =cap.read()
    print(ret)
    print(frame)
else:
    ret = False
    img1= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    plt.imshow(img1)
    plt.title('Capture Image-1')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    cap.release()