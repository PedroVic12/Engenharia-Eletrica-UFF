import cv2
import numpy as np
import hand_tracking_module as htm
import time
import pyautogui
from ia_module import IAModuleCV

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
wScr, hScr = pyautogui.size()
#########################

pyautogui.FAILSAFE = False

def setup():

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = htm.handDetector()
    return (
        cap,
        detector,
    )


def showLandMakers():
    hand = ia_module.hands_mediaPipe()
    resultados = hand.process(RBG_frame)
    if resultados.multi_hand_landmarks:
        for hand_landmarks in resultados.multi_hand_landmarks:
            print(hand_tracking_module)


def main_ia_virtualMouse():
    cap, detector = setup()
    ia_module = IAModuleCV()

    print("IA VIRTUAL MOUSE")

    while True:

        # 1. Find hand Landmarks
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        RBG_frame = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)


        
        # 2. Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            # print(x1, y1, x2, y2)

            # 3) Check witch fingers
            fingerts = detector.fingersUp()
            print(fingerts)


            #4),5,6,7
            ia_module.desenhaRetangulo(img,(frameR,frameR), (wCam-frameR,hCam-frameR))
            ia_module.movingMode(fingerts,x1,y1,[wCam,hCam],[wScr,hScr])
            ia_module.desenhaCirculo(img,x1,y1)


            #8) both index and middle finger -> clicking mode

            # 9 find distance between fingers

            # 10 click mouse if distance short


            # 11 frame rate
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            #pTime = cTime
            cv2.putText(img,str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3,255,0,0,3)

        # 12 display
        ia_module.showCV(img)

main_ia_virtualMouse()