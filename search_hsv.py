import cv2


#img = cv2.VideoCapture(0)
#img = cv2.imread('test1.jpg')
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def mouse_click(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONDOWN: #滑鼠左鍵
        print(x,y)
        print(hsv[y,x])
        print(flags , para)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('image')#建立視窗
    cv2.setMouseCallback('image', mouse_click)#在image視窗上設定滑鼠事件
    while True:
        ret , frame = cap.read()
        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow('image', frame)
        else:
            break
        if cv2.waitKey(1)  == ord('q'):
            break
