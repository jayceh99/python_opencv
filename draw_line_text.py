import cv2
import numpy as np

img = np.zeros((600,600,3) , np.uint8) #np.zeros創建的陣列內容會是0大小為600x600的圖片，3表示RGB三個通道，uint8表示正整數8位元組


cv2.line(img, (0,0) , (600,600), (255,255,255), 5) #cv2.line畫直線，(0,0)為起點左上角，(600,600)為終點右下角，(255,255,255)為顏色，5為線寬度
cv2.line(img, (0,0) , (img.shape[1],img.shape[0]), (255,255,255), 5) #img.shape[1]為寬，img.shape[0]為高
cv2.rectangle(img, (200,200), (400,400), (0,0,255), cv2.FILLED) #cv2.rectangle畫矩形，(200,200)為左上角，(400,400)為右下角，(0,0,255)為顏色，cv2.FILLED為填滿整個矩形
cv2.circle(img, (300,300), 50, (0,255,0), 5) #cv2.circle畫圓形，(300,300)為中心點，50為半徑，(0,255,0)為顏色，5為邊框寬度
cv2.putText(img, 'OpenCV', (100,500), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2) #cv2.putText在圖片上寫字，'OpenCV'為文字，(100,500)為文字位置，cv2.FONT_HERSHEY_PLAIN為字型，2為字型大小，(255,255,255)為字型顏色，2為邊框寬度，cv2.LINE_AA為文字輪廓
#cv2.putText不支援中文!


cv2.imshow('image', img)

cv2.waitKey(0)