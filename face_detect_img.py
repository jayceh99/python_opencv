import cv2


img = cv2.imread('lenna.jpg')
img = cv2.imread('test123.jpg')
img = cv2.resize(img, (640, 480)) #調整圖片大小
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_detect = cv2.CascadeClassifier('face_detect.xml') 
#可以在opencv的github找到 https://github.com/opencv/opencv/tree/4.x/data/haarcascades/haarcascade_frontalface_default.xml
#裡面還有很多很好玩的模組
faceRect = face_detect.detectMultiScale(gray, 1.1, 5) #1.圖片縮放比例，2.圖片縮小倍數，3.臉要被框到幾次才算偵測到 越大越嚴謹 反之
#會用一堆小框框偵測
# 人臉 直到整張圖片偵測完 有偵測到人臉就會記錄下來 偵測完一輪 就會把圖片縮小然後繼續偵測
print(len(faceRect))
for (x , y , w , h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('img', img)

cv2.waitKey(0)
