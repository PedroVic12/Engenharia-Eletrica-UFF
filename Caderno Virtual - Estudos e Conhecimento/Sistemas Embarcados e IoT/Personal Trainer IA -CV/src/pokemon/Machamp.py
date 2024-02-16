import cv2
from PIL import Image
import numpy as np
import pandas as pd
import time
from src.models.poseModule import poseDetector


class DataExploration:
    def __init__(self):
        pass

    df = pd.DataFrame(columns=["Frame", "RightArmAngle", "LeftArmAngle"])
    dados = []
    frame_count = 0


class Machamp:
    def __init__(self):
        self.name = "Machamp"
        self.type = "Fighting"
        self.level = 100
        self.hp = 90
        self.attack = 130
        self.defense = 80
        self.special_attack = 65
        self.special_defense = 85
        self.speed = 55
        self.moves = ["Cross Chop", "Dynamic Punch", "Earthquake", "Fire Blast"]
        self.stats = [
            self.hp,
            self.attack,
            self.defense,
            self.special_attack,
            self.special_defense,
            self.speed,
        ]
        self.current_hp = self.hp

        #!VARIAVEIS
        self.color = (255, 0, 255)
        self.bar = 0
        self.percentual = 0
        self.pTime = 0
        self.MAP = {}
        self.contador = 0
        self.dir = None  # None significa que ainda não começou a se mover
        self.limite_superior = (
            50  # Definir conforme observado para o movimento completo
        )
        self.limite_inferior = 0  # Definir conforme observado para o movimento completo

    def __str__(self):
        return self.name

    def openImage(self, img):
        cv2.imshow("Image", img)
        while True:
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()

    def detectarFaces(self, imgGray, img, detector):
        faces = detector.detectMultiScale(imgGray, 1.1, 4)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(
                img, "Face", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2
            )

    def exibir_imagem(self, img):
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()

    def abrir_imagem(self, path):
        imagem = Image.open(path)
        img_np = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)
        return img_np

    def abrir_video(self, path):
        cap = cv2.VideoCapture(path)
        success, img = cap.read()
        return img if success else None

    def processVideo(self, img, detector):
        # right arm
        right_arm_angle = round(detector.findAngle(img, 12, 14, 16), 2)
        print("\n\nRIGHT", right_arm_angle)

        # left arm
        left_arm_angle = round(detector.findAngle(img, 11, 13, 15), 2)
        print("LEFT", left_arm_angle)

        # Percentual de execução
        self.percentual = np.interp(left_arm_angle, (210, 310), (0, 100))
        self.bar = np.interp(left_arm_angle, (220, 310), (650, 100))
        print(f"Percentual = {   self.percentual }%")

        # Adiciona os dados coletados na lista
        self.MAP["RightArmAngle"] = right_arm_angle
        self.MAP["LeftArmAngle"] = left_arm_angle

        self.exercise_counter(self.percentual)
        self.drawInScreen(img)

    def exercise_counter(self, per):
        # Mudança de direção para cima
        if per >= self.limite_superior and self.dir != 1:
            self.color = (0, 255, 0)
            self.dir = 1  # Movendo para cima
            self.contador += 0.5  # Incrementa a contagem na mudança de direção

        # Mudança de direção para baixo
        elif per <= self.limite_inferior and (self.dir is None or self.dir == 1):
            self.color = (0, 255, 0)
            if self.dir == 1:  # Apenas conta se estava se movendo para cima antes
                self.contador += 0.5
            self.dir = 0  # Movendo para baixo

        if self.contador == 5:
            print("Executou 5 repetições")

        print(f"Contagem = {int(self.contador)}")

    def temporizador(self, img):
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        return fps

    def drawInScreen(self, _img):
        # Por exemplo, aumentar para o dobro da largura e altura
        img = cv2.resize(_img, (0, 0), fx=4, fy=2)

        fps = self.temporizador(img)

        cv2.putText(
            img,
            f"FPS: {int(fps)}",
            (10, 70),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255, 0, 0),
            3,
        )

        # Desenha as linhas que representam os limites superior e inferior
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)

        cv2.putText(
            img,
            f"{int(self.contador)}",
            (45, 670),
            cv2.FONT_HERSHEY_PLAIN,
            12,
            (255, 0, 0),
            25,
        )

        cv2.rectangle(
            img,
            (1100, 100),
            (1175, 650),
            (0, 255, 0),
            3,
        )
        cv2.rectangle(
            img,
            (1100, int(self.bar)),
            (1175, 650),
            self.color,
            cv2.FILLED,
        )
        cv2.putText(
            img,
            f"{int(self.percentual)}%",
            (1100, 75),
            cv2.FONT_HERSHEY_PLAIN,
            4,
            self.color,
            4,
        )

        self.exibir_imagem(img)
