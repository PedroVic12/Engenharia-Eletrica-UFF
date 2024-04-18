import cv2
import numpy as np
import hand_tracking_module as htm
import time
import pyautogui

# import autopy
import mediapipe as mp


class IAModuleCV:
    def __init__(self):
        pass

    def showCV(self, img):
        cv2.imshow("Tela", img)
        cv2.waitKey(1)

    def displayText(self, text):
        cv2.putText(text, (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, 255, 0, 0, 3)

    def desenhaRetangulo(self, img, x1, y1):
        try:
            cv2.rectangle(img, x1, y1, (255, 0, 255), 2)
        except:
            print("erro")

    def desenhaCirculo(self, img, x1, y1):
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

    def movingMode(self, fingers, x1, y1, camera_arr, screen_arr, frame):
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. converter em coordenadas
            x3 = np.interp(x1, (frame, camera_arr[0] - frame), (0, screen_arr[0]))
            y3 = np.interp(y1, (frame, camera_arr[1] - frame), (0, screen_arr[1]))
            print(f"Coordenadas = {x3} x {y3}")
            return x3, y3

    # return x3, y3

    def clickingMode(self, dedos, detector, img):
        if dedos[1] == 1 and dedos[2] == 1:
            tamanho, img, line_info = detector.findDistance(8, 12, img)
            return tamanho, line_info

    def hands_mediaPipe(self):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        return hands

    def displayMediaPipe(self):
        # STEP 1: Import the necessary modules.
        import mediapipe as mp
        from mediapipe.tasks import python
        from mediapipe.tasks.python import vision

        # STEP 2: Create an HandLandmarker object.
        base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
        options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
        detector = vision.HandLandmarker.create_from_options(options)

        # STEP 3: Load the input image.
        image = mp.Image.create_from_file("image.jpg")

        # STEP 4: Detect hand landmarks from the input image.
        detection_result = detector.detect(image)

        # STEP 5: Process the classification result. In this case, visualize it.
        annotated_image = htm.draw_landmarks_on_image(
            image.numpy_view(), detection_result
        )
        cv2.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))