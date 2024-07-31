import cv2

'''
img = cv2.imread('test.jfif')
#img = cv2.resize(img, (200, 200))#縮放大小
img = cv2.resize(img, (0, 0) , fx=0.3, fy=0.3) #縮放倍數
cv2.imshow('image', img)
cv2.waitKey(0)
'''

face_detect = cv2.CascadeClassifier('face_detect.xml') 
#face_detect = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
#face_detect = cv2.CascadeClassifier('smile_detect.xml')
#face_detect = cv2.CascadeClassifier('upper_body_detect.xml') 
#cap = cv2.VideoCapture('test.mp4') #讀影片
cap = cv2.VideoCapture(0) #開啟第0個攝像頭
while True:
    ret , frame = cap.read()  #讀取一楨 ret為布林值，frame為影像楨

    if ret == True:
        frame = cv2.resize(frame, (600, 450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRect = face_detect.detectMultiScale(gray, 1.1, 5) #1.圖片縮放比例，2.圖片縮小倍數，3.臉要被框到幾次才算偵測到 越大越嚴謹 反之
        print(faceRect)
# 人臉 直到整張圖片偵測完 有偵測到人臉就會記錄下來 偵測完一輪 就會把圖片縮小然後繼續偵測
        #print(len(faceRect))
        for (x , y , w , h) in faceRect: #x座標 y座標 寬度 高度
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            
        cv2.imshow('frame', frame)
            #print('OK')
    else:
        break
    if cv2.waitKey(1)  == ord('q'): #按q離開迴圈

        break