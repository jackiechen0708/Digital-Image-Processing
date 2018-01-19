import cv2
import  numpy as np
import math
transformation=np.array([[1,0],[0,1]])
theta=math.pi/4
rotation=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
theta=-math.pi/4
rotation2=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])

theta=math.pi/16
skew=np.array([[1,0],[math.tan(theta),1]])

theta=math.pi/16
skew2=np.array([[1,math.tan(theta)],[0,1]])

theta=math.pi/16
skew2=np.array([[1,math.tan(theta)],[0,1]]).dot(skew)

img=cv2.imread("pkq.jpg")
new_img=np.zeros_like(img,np.uint8)


homogenous_matrix=np.array([[1,0,20],[0,1,50],[0,0,1]])




for h in range(img.shape[0]):
    for w in range(img.shape[1]):
        # new_h,new_w=rotation2.dot(rotation.dot(np.array([h-img.shape[0]/2,w-img.shape[1]/2])))
        # new_h,new_w=int(new_h)+img.shape[0]/2,int(new_w)+img.shape[1]/2
        # new_h,new_w=skew2.dot(np.array([h-img.shape[0]/2,w-img.shape[1]/2]))
        # new_h, new_w = int(new_h) + img.shape[0] / 2, int(new_w) + img.shape[1] / 2
        new_h, new_w ,_=homogenous_matrix.dot(np.array([h,w,1]))
        # new_h, new_w = int(new_h) + img.shape[0] / 2, int(new_w) + img.shape[1] / 2
        print (new_h,new_w)
        if (0<=new_h<img.shape[0] and 0<=new_w<img.shape[1]):
            new_img[h,w]=img[new_h,new_w]
cv2.imshow("original",img)
cv2.imshow("new",new_img)
cv2.waitKey(0)
