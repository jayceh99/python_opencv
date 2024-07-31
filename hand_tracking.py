import cv2
import mediapipe as mp
import math
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(255,0,0) , thickness=2)#改變點的樣式
hanconStyle = mpDraw.DrawingSpec(color=(0,255,0) , thickness=10)#改變線的樣式
cap = cv2.VideoCapture(0)
#mphands = mp.solutions


while True:
    ret , frame = cap.read()
    if ret == True:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        frame = cv2.resize(frame, (640, 480))
        #print(frame.shape[1])
        #print(frame.shape[0])
        #print(result.multi_hand_landmarks)
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLms, mphands.HAND_CONNECTIONS , handLmsStyle , hanconStyle)  
                for i , lm in enumerate(handLms.landmark):#i為第幾個點 lm為該點的座標
                    xPos = int(lm.x * frame.shape[1])#lm.x , lm.y 為x,y座標 0~1之間 為比例 要找到真正的座標只要乘上寬高即可
                    yPos = int(lm.y * frame.shape[0])
                    #print(i , xPos , yPos ) 
                    cv2.putText(frame ,str(i), (xPos , yPos) , cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
                    
                    if i == 4:
                        Thumbdis = [xPos, yPos]
                    if i == 8:
                        Indexdis = [xPos, yPos]
                    if i == 12 :
                        Middledis = [xPos, yPos]
                    if i == 13:
                        Handdis = [xPos , yPos]
                    if i == 16:
                        Ringdis = [xPos, yPos]
                    if i == 20:
                        Pinkydis = [xPos, yPos]
                #dis = math.hypot(Ringdis[0]-Thumbdis[0], Ringdis[1]-Thumbdis[1])
                #print(math.hypot(Thumbdis[0]-Handdis[0], Thumbdis[1]-Handdis[1]))
                if math.hypot(Thumbdis[0]-Handdis[0], Thumbdis[1]-Handdis[1]) > 150:
                    print("讚")
                else :
                    print("不讚")
            

        cv2.imshow('frame' , frame)
    else:
        break
    if cv2.waitKey(1) == ord('q') :
        break