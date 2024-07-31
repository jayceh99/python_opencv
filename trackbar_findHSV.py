import cv2
import numpy as np
def empty(v):
    pass
img = cv2.imread('test1.jpg')
img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
cv2.namedWindow("trackbar")#動態控制條 找出適合的參數
cv2.resizeWindow("trackbar", 640, 320)#調整視窗大小
cv2.createTrackbar("Hue Min" , "trackbar" , 0 , 179 , empty)# 1.控制條名稱 2.視窗名稱 3.初始值 4.最大值 hue值0~179 ,5.當控制條被改變要呼叫的函式
cv2.createTrackbar("Hue Max" , "trackbar" , 179 , 179 , empty)
cv2.createTrackbar("sat Min" , "trackbar" , 0 , 255 , empty)
cv2.createTrackbar("sat Max" , "trackbar" , 0 , 255 , empty)
cv2.createTrackbar("val Min" , "trackbar" , 0 , 255 , empty)
cv2.createTrackbar("val Max" , "trackbar" , 255 , 255 , empty)
#HSV 由色調(Hue)、飽和度(Saturation)、明度(Value)組成，H的取值範圍為0~179，S的取值範圍為0~255，V的取值範圍為0~255。


hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)#RGB轉成HSV
while True:
    h_Min =  cv2.getTrackbarPos("Hue Min" , "trackbar" )
    h_Max =  cv2.getTrackbarPos("Hue Max" , "trackbar" )
    s_Min =  cv2.getTrackbarPos("sat Min" , "trackbar" )
    s_Max =  cv2.getTrackbarPos("sat Max" , "trackbar" )
    v_Min =  cv2.getTrackbarPos("val Min" , "trackbar" )
    v_Max =  cv2.getTrackbarPos("val Max" , "trackbar" )
    print(h_Min,h_Max,s_Min,s_Max,v_Min,v_Max)


    lower = np.array([h_Min, s_Min, v_Min])
    upper = np.array([h_Max, s_Max, v_Max])
    

    mask =  cv2.inRange(hsv , lower , upper ) #過濾顏色 1.要過濾的圖片 2.最小值 3.最大值  最小最大值要越array表示
    result = cv2.bitwise_and(img , img , mask = mask) #過濾後的結果 1.原圖 2.原圖 3.過濾後的mask 會把 1,2兩張圖片做AND運算做完之後在套上MASK的遮罩
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('img', img)
    cv2.waitKey(1)
    #調整控制條  黑色是被過濾掉的部分
cv2.imshow('hsv', hsv)
cv2.waitKey(0)



