import cv2

'''
img = cv2.imread('test.jfif')
#img = cv2.resize(img, (200, 200))#縮放大小
img = cv2.resize(img, (0, 0) , fx=0.3, fy=0.3) #縮放倍數
cv2.imshow('image', img)
cv2.waitKey(0)
'''


cap = cv2.VideoCapture('test.mp4') #讀影片
#cap = cv2.VideoCapture(0) #開啟第0個攝像頭
while True:
    ret , frame = cap.read()  #讀取一楨 ret為布林值，frame為影像楨

    if ret == True:
        frame = cv2.resize(frame, (200, 200))
        
        cv2.imshow('frame', frame)
    else:
        break
    if cv2.waitKey(1)  == ord('q'): #按q離開迴圈

        break