import cv2
import numpy as np
import time

from src.models.poseModule import poseDetector

import os


def processar_imagens_diretorio(pokemon, detector, diretorio):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".png"):
            caminho_completo = os.path.join(diretorio, arquivo)
            img = pokemon.abrir_imagem(caminho_completo)
            img = cv2.resize(img, (500, 400))  # Ajuste o tamanho conforme necessário
            img = detector.findPose(img, draw=True)
            print(f"Processando {arquivo}...")
            pokemon.exibir_imagem(img)
            cv2.waitKey(
                0
            )  # Espera uma tecla ser pressionada para processar a próxima imagem
    cv2.destroyAllWindows()


def teste():
    cap = cv2.VideoCapture(0)  # Use 0 para a webcam padrão
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # Pressione 'q' para sair
            break

    cap.release()
    cv2.destroyAllWindows()


def contador():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
        )

        cv2.imshow("Image", img)
        cv2.waitKey(1)
