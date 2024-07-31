import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8) #5x5的陣列 值為0~255
img = cv2.imread('test.jfif')
img = cv2.resize(img , (0,0) , fx=0.2 , fy=0.2)
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)#灰階處理
blur = cv2.GaussianBlur(img ,(9,9) , 5)#高斯模糊 去除躁點 1.處理的圖片 2.kernel和的大小需奇數 3,3 5,5 7,7 etc... 3.標準差   更改kernel及標準差 可調整模糊程度
canny = cv2.Canny(img, 100 , 150) #邊緣檢測 1.處理的圖片 2.最小值 3.最大值 邊緣檢測原理對比周邊像數值 差別很大即判斷是輪廓
dilate = cv2.dilate(canny , kernel=kernel , iterations=3) #膨脹 1.處理的圖片 2.kernel值 二維陣列 3.膨脹次數  陣列大小以及膨脹次數決定粗度(應該是可以理解成粗體) 
erode = cv2.erode(dilate  , kernel=kernel , iterations=5)#輕實 跟膨脹相反 變細

cv2.imshow('img' , img)
cv2.imshow('gray' , gray)
cv2.imshow('blur' ,blur)
cv2.imshow('canny' , canny)
cv2.imshow('dilate' , dilate)
cv2.imshow ('erode' , erode)
cv2.waitKey(0)
