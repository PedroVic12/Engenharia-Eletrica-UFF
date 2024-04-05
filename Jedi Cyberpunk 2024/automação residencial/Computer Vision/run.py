import cv2
import numpy as np
import hand_tracking_module as htm
import time
import pyautogui
from ia_module import IAModuleCV
import mediapipe as mp
import threading

ia_module = IAModuleCV()

# Largura e altura da câmera
wCam, hCam = 640, 480
# Redução do frame
frameR = 100
# Suavização do movimento do mouse
smoothening = 7
# Tempo de início
pTime = 0

cTime = 0

# Coordenadas do mouse (anterior e atual)
plocX, plocY = 0, 0
clocX, clocY = 0, 0
# Largura e altura da tela
wScr, hScr = pyautogui.size()

# Configuração da câmera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Inicialização do detector de mãos
detector = htm.handDetector(max_hands=1)

def show_opencv_window():
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        RBG_frame = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            dedos = detector.fingersUp()
            ia_module.desenhaRetangulo(img, (frameR, frameR), (wCam - frameR, hCam - frameR))

            try:  
                x3, y3 = ia_module.movingMode(dedos, x1, y1, [wCam, hCam], [wScr, hScr], frameR)
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                pyautogui.moveTo(wScr - clocX, clocY)
                plocX, plocY = clocX, clocY

                if x3 and y3:
                    pyautogui.move(x3, y3)
            except:
                print("Erro ao tentar mover")
            
            ia_module.desenhaCirculo(img, x1, y1)

            try:
                tamanho, line_info = ia_module.clickingMode(dedos, detector, img)
                if tamanho < 40:
                    pyautogui.moveTo(0, 0)
                    pyautogui.click()
            except:
                print("Erro ao clicar")

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, 255, 0, 0, 3)

        ia_module.showCV(img)
        pTime = cTime

def show_pyautogui_window():
    while True:
        # Atualizar a tela do PyAutoGUI
        print("updating...")
        #pyautogui.screenshot()
        # Adicionar qualquer outra operação necessária para atualizar a tela

# Criar e iniciar as threads
thread_opencv = threading.Thread(target=show_opencv_window)
thread_opencv.start()

thread_pyautogui = threading.Thread(target=show_pyautogui_window)
thread_pyautogui.start()

# Aguardar até que as threads terminem (o que nunca deve acontecer)
thread_opencv.join()
thread_pyautogui.join()
