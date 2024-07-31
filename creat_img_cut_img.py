import cv2
import numpy as np
import random
img = cv2.imread('test.jfif')
""" # print(img.shape)

# img = np.empty((300,300,3) , np.uint8) #uint 表示正整數 8 表示2^8

# for raw in range(300):
#     for col in range(300):
#         img[raw][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)] #隨機產生0~255的BGR值

 """
newimg = img[:150,:150] #切割圖片
cv2.imshow('newimg',newimg)
cv2.imshow('img',img)
cv2.waitKey(0)

# img = cv2.resize(img , (0 , 0) , fx=0.2, fy=0.2)
# cv2.imshow('img',img)
# cv2.waitKey(0)
