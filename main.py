# https://google.github.io/mediapipe/solutions/hands
import cv2
import mediapipe as mp
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    idmark=[]
    fingertip = [8,12,16,20]
    # https://google.github.io/mediapipe/solutions/hands

    if results.multi_hand_landmarks:
        #deect points
        for handLms in results.multi_hand_landmarks:
            #color circle at id point
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                #converting ratio to 
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                idmark.append([id, cx, cy])
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            
            keyboard.release(Key.left)
            keyboard.release(Key.enter)
            keyboard.release(Key.right)
            if idmark[8][2] < idmark[8-2][2] or idmark[8-1][2]<idmark[8-2][2]:
                if idmark[12][2] < idmark[12-2][2] or idmark[12-1][2]<idmark[12-2][2]:
                    if idmark[16][2] < idmark[16-2][2] or idmark[16-1][2]<idmark[16-2][2]:
                        if idmark[20][2] < idmark[20-2][2] or idmark[20-1][2]<idmark[20-2][2]:
                            print('Acelerate')
                            # keyboard.release(Key.enter)
                            # keyboard.release(Key.left)
                            keyboard.press(Key.right)
            else:
                print('Brake')
                # keyboard.release(Key.enter)
                # keyboard.release(Key.right)
                keyboard.press(Key.left)



            if(idmark[8][2] < idmark[8-2][2] or idmark[8-1][2]<idmark[8-2][2]):
                if idmark[12][2] < idmark[12-2][2] or idmark[12-1][2]<idmark[12-2][2]:
                    if idmark[16][2] > idmark[16-2][2] or idmark[16-1][2]>idmark[16-2][2]:
                        if idmark[20][2] > idmark[20-2][2] or idmark[20-1][2]>idmark[20-2][2]:
                            print('Enter')
                            # keyboard.release(Key.left)
                            # keyboard.release(Key.right)
                            keyboard.press(Key.enter)







            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    #frame per second
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)  