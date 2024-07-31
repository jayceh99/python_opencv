import cv2

img = cv2.imread('shape.jpg')
imgContour = img.copy()#複製一張圖片
img = cv2.cvtColor(img  , cv2.COLOR_BGR2GRAY)#轉成灰階 辨識輪廓不需要顏色
canny = cv2.Canny(img , 150 , 200)#Canny邊緣偵測
contours , hierarchy = cv2.findContours(canny , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE) #1.要偵測的圖片 2.偵測模式(內輪廓或外輪廓或內外都要)這邊選外輪廓 3.近似方法 壓縮垂直或是水平 這邊選不壓縮
#會回傳兩個參數，一個是輪廓陣列，一個是輪廓的階層結構

for cnt in contours:
    #print(cnt)
    #把找到的輪廓點都印出來
    cv2.drawContours(imgContour, cnt, -1 , (0, 255, 0) , 3) #把找到的輪廓畫出來 1.圖片 2.輪廓陣列 3.輪廓編號(-1代表全部) 4.顏色 5.線條寬度
    #print(cv2.contourArea(cnt)) #算每一個輪廓面積
    area = cv2.contourArea(cnt)
    if area > 500: #只要面積大於500的輪廓 過濾躁點
        #print(cv2.arcLength(cnt,True)) #算輪廓周長 1.輪廓陣列 2.是否封閉
        peri = cv2.arcLength(cnt,True)
        vertix = cv2.approxPolyDP(cnt , peri * 0.02, True)
        #多邊形近似 1.輪廓陣列 2.近似值 越大多邊形越多 設定為輪廓邊長的.22倍 可自定義 3.是否封閉
        print(len(vertix)) #查看圖片幾個頂點 猜測是甚麼形狀
        corners = len(vertix)
        x , y , w , h = cv2.boundingRect(vertix) #把形狀用方型框起來 找出 四個頂點的座標
        cv2.rectangle(imgContour , (x,y) , (x+w,y+h) , (255,0,0) , 2) #畫方型框 1.圖片 2.左上角座標 3.右下角座標 4.顏色 5.線條寬度
        if corners == 3:
            cv2.putText(imgContour, "Triangle" , (x,y-5) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0) , 2)
            #文字顯示 1.圖片 2.文字 3.文字位置 4.字型 5.大小 6.顏色 7.線條寬度
        elif corners == 4:
            cv2.putText(imgContour, "Rectangle" , (x,y-5) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0) , 2)
        elif corners == 5:
            cv2.putText(imgContour, "Pentagon" , (x,y-5) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0) , 2)
        elif corners >= 6:
            cv2.putText(imgContour, "Cicrle" , (x,y-5) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0) , 2)
cv2.imshow('image', img)
cv2.imshow('canny', canny)
cv2.imshow('contour', imgContour) #顯示輪廓圖片
cv2.waitKey(0)