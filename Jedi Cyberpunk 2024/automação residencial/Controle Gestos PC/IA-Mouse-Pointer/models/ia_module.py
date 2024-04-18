import cv2
import numpy as np
import hand_tracking_module as htm
import time
import pyautogui

class IAModuleCV:
	def __init__(self):
		pass

	def showCV(img):
		cv2.imshow("Tela", img)
		cv2.waitKey(1)


	def displayText(self,text):
	    cv2.putText(text, (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, 255, 0, 0, 3)

	def desenhaRetangulo(self,img, x1, y1):
		cv2.rectangle(img,(x1,y1),(255, 0, 255), 2)

	def desenhaCirculo(self,img, x1, y1):
	    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

	def frame_rate():
		cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(
            img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, 255, 0, 0, 3
        )

	def movingMode(self,fingers, x1, y1, WCam, h):
	    if fingers[1] == 1 and fingers[2] == 0:
	        # 5. converter em coordenadas
	        x3 = np.interp(x1, (0, wCam), (0, wScr))
	        y3 = np.interp(y1, (0, wCam), (0, hScr))

	        # 6 smothen values

	        # 7 move mouse
	        pyautogui.move(x3, y3)
