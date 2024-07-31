import cv2
import numpy as np

'''
img = cv2.imread('test.jfif')
#img = cv2.resize(img, (200, 200))#縮放大小
img = cv2.resize(img, (0, 0) , fx=0.3, fy=0.3) #縮放倍數
cv2.imshow('image', img)
cv2.waitKey(0)
'''

draw = []
color = [[77,163 ,92,255,81,255],
         [0,10,148,218,131,255]]

paint_color = [[255, 0, 0],
               [0, 0, 255]]
# [x , y , color] 
def find_pen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #轉換成HSV色彩空間
    #109 152 119
    for i in range (len(color)):
        lower = np.array([color[i][0], color[i][2], color[i][4]])
        upper = np.array([color[i][1], color[i][3], color[i][5]])
        #lower = np.array([65, 106, 175])
        #upper = np.array([185, 234, 235])
        mask =  cv2.inRange(hsv , lower , upper ) #過濾顏色 1.要過濾的圖片 2.最小值 3.最大值  最小最大值要越array表示
        result = cv2.bitwise_and(img, img , mask = mask) #過濾後的結果 1.原圖 2.原圖 3.過濾後的mask 會把 1,2兩張圖片做AND運算做完之後在套上MASK的遮罩
        penx , peny = find_contours(mask)
        cv2.circle(imgcontour, (penx, peny), 5, paint_color[i], cv2.FILLED) #畫出找到的筆的頂點
        #cv2.imshow('result', result)
        if peny != -1:
            draw.append([penx, peny, i]) #把筆的座標和顏色存進draw陣列
        
    return result

def find_contours(img):

    contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE) #1.要偵測的圖片 2.偵測模式(內輪廓或外輪廓或內外都要)這邊選外輪廓 3.近似方法 壓縮垂直或是水平 這邊選不壓縮
#會回傳兩個參數，一個是輪廓陣列，一個是輪廓的階層結構
    x , y , w ,h = -1 , -1 ,-1 ,-1
    for cnt in contours:
        #print(cnt)
        #把找到的輪廓點都印出來
        cv2.drawContours(imgcontour, cnt, -1 , (0, 255, 0) , 3) #把找到的輪廓畫出來 1.圖片 2.輪廓陣列 3.輪廓編號(-1代表全部) 4.顏色 5.線條寬度
        #print(cv2.contourArea(cnt)) #算每一個輪廓面積
        area = cv2.contourArea(cnt)
        if area > 500: #只要面積大於500的輪廓 過濾躁點
            #print(cv2.arcLength(cnt,True)) #算輪廓周長 1.輪廓陣列 2.是否封閉
            peri = cv2.arcLength(cnt,True)
            vertix = cv2.approxPolyDP(cnt , peri * 0.02, True)
            #多邊形近似 1.輪廓陣列 2.近似值 越大多邊形越多 設定為輪廓邊長的.22倍 可自定義 3.是否封閉
            x , y , w , h = cv2.boundingRect(vertix) #把形狀用方型框起來 找出 四個頂點的座標
    return x+w//2 , y       
    
def draw_line(draw):
    for point in draw:
        cv2.circle(imgcontour, (point[0], point[1]), 5, paint_color[point[2]], cv2.FILLED) #畫出筆的座標和顏色

#cap = cv2.VideoCapture('test.mp4') #讀影片
cap = cv2.VideoCapture(0) #開啟第0個攝像頭
while True:
    ret , frame = cap.read()  #讀取一楨 ret為布林值，frame為影像楨

    if ret == True:
        
        frame = cv2.resize(frame, (900, 600))
        imgcontour = frame.copy()
        result = find_pen(frame)
        draw_line(draw)
        cv2.imshow('result', result)
        cv2.imshow('frame', imgcontour)
        #cv2.imshow('frame', frame)
        
    else:
        break
    if cv2.waitKey(1)  == ord('q'): #按q離開迴圈

        break
