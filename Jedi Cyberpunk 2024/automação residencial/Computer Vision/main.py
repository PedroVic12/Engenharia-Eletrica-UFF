import cv2
import numpy as np
import hand_tracking_module as htm
import time
import pyautogui
from ia_module import IAModuleCV
import mediapipe as mp


ia_module = IAModuleCV()

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
wScr, hScr = pyautogui.size()
print(wScr,hScr)
#########################

pyautogui.FAILSAFE = False

def setup():

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = htm.handDetector(max_hands = 1)
    return (
        cap,
        detector,
    )


def showLandMakers(RBG_frame):
    hand = ia_module.hands_mediaPipe()
    resultados = hand.process(RBG_frame)
    if resultados.multi_hand_landmarks:
        for hand_landmarks in resultados.multi_hand_landmarks:
            print(hand_landmarks)


def main_ia_virtualMouse():
    cap, detector = setup()

    print("IA VIRTUAL MOUSE")

    while True:

        # 1. Find hand Landmarks
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        RBG_frame = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)
        #showLandMakers(RBG_frame)

        # 2. Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            # 3) Check witch fingers
            dedos = detector.fingersUp()
            print(dedos)


            #4),5,6
            ia_module.desenhaRetangulo(img,(frameR,frameR), (wCam-frameR,hCam-frameR))
            try:  

                x3,y3 = ia_module.movingMode(dedos,x1,y1,[wCam,hCam],[wScr,hScr],frameR)

            # 7 move mouse
            #ia_module.moverMouseSuave(clocX,clocY,plocX,plocY,smoothening,x3,y3)
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                pyautogui.move(wScr - clocX, clocY)
                plocX,plocY = clocX, clocY


                if x3 and y3:
                    print("movendo normal")
                    pyautogui.move(x3, y3)

            except:
                print("Erro ao tentar mover")
            #autopy.mouse.move(screen_arr[0] - x3, y3)

            ia_module.desenhaCirculo(img,x1,y1)


            #8) both index and middle finger -> clicking mode
            try:
                tamanho, line_info = ia_module.clickingMode(dedos,detector,img)
                # 9 find distance between fingers
                print(tamanho)
                if tamanho < 40:
                    # 10 click mouse if distance short
                    ia_module.desenhaCirculo(img,line_info[4],line_info[5])
                    pyautogui.click()
                else:
                    print("valor vazio")
            except:
                print("Erro ao clicar")



            # 11 frame rate
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            #pTime = cTime
            cv2.putText(img,str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3,255,0,0,3)

        # 12 display
        ia_module.showCV(img)

main_ia_virtualMouse()