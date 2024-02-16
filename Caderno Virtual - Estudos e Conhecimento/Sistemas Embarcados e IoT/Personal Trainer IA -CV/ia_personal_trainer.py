import cv2
import numpy as np
import time

from src.models.poseModule import poseDetector
from src.utils import utils_functions
import pandas as pd
from src.pokemon.Machamp import Machamp

#!TODO 28:18

# todo processar o minimo e maximo do movimento
# todo contador de movimentos
# todo classificar em movimento limpo ou nao
# todo calcular cadencia do movimento
# data view ao mesmo tempo
# integracao com flutter

detector = poseDetector()
pokemon = Machamp()


def loop_trainer_video():
    cap = cv2.VideoCapture("Personal Trainer IA -CV/assets/flexao_normal.mp4")

    # Iniciar o processamento de vídeo
    while True:
        success, img = cap.read()
        if not success:
            break

        # Definir as propriedades do vídeo de saída
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_size = (
            int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 4),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 2),
        )  # Ajustar conforme o redimensionamento
        out = cv2.VideoWriter("./saida_video.mp4", fourcc, fps, frame_size)

        # Processar a imagem
        img = detector.findPose(img, draw=True)
        lmList = detector.findPosition(img, draw=False)
        # print(f"Coordenadas PIPELINE = {lmList}")

        # Verifica se tem alguem
        if len(lmList) != 0:
            pokemon.processVideo(img, detector)

        # Redimensionar para o tamanho de saída antes de escrever
        img_resized = cv2.resize(img, frame_size)
        out.write(img_resized)
        # pokemon.exibir_imagem(img)

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def loop_trainer_foto():

    # Se você quiser processar uma imagem estática, faça fora do loop
    img_estatica = pokemon.abrir_imagem(
        "Personal Trainer IA -CV/assets/barra_completa.png"
    )
    img_estatica = cv2.resize(img_estatica, (500, 400))

    # Processar a imagem estática
    img_estatica = detector.findPose(img_estatica, draw=True)
    lmList = detector.findPosition(img_estatica, draw=True)

    # Verifica se tem alguém
    if len(lmList) != 0:
        # right arm
        angle = round(detector.findAngle(img_estatica, 12, 14, 16), 2)
        print("RIGHT", angle)
        per = np.interp(angle, (210, 310), (0, 100))
        barra = np.interp(angle, (220, 310), (400, 150))

        # left arm
        angle = detector.findAngle(img_estatica, 11, 13, 15)
        print("LEFT", angle)

    pokemon.openImage(img_estatica)
    time.sleep(15)  # Exibe por 5 segundos e depois começa a processar o vídeo


if __name__ == "__main__":
    # loop_trainer_foto()
    loop_trainer_video()

    # utils_functions.processar_imagens_diretorio(
    #   pokemon, detector, "Personal Trainer IA -CV/assets"
    # )
