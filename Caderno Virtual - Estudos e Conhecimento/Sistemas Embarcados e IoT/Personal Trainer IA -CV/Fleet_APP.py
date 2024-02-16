import flet as ft
import cv2
import numpy as np
from src.models.poseModule import poseDetector

detector = poseDetector()


def main(page: ft.Page):
    page.title = "Detecção de Pose com Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criação dos elementos da UI
    video_player = ft.UserContent()
    angles_text = ft.Text(value="Ângulos: ", size=20)

    page.add(video_player, angles_text)

    # Configuração da câmera
    video_source = "Personal Trainer IA -CV/assets/flexao_normal.mp4"

    cap = cv2.VideoCapture(video_source)  # Use 0 para webcam

    def update_frame():
        # Captura um frame
        success, img = cap.read()
        if not success:
            print("Falha ao capturar imagem da câmera.")
            return

        # Processa o frame para detecção de pose
        img = detector.findPose(img, draw=True)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            # Exemplo: calcular ângulo do braço direito
            right_arm_angle = round(detector.findAngle(img, 12, 14, 16), 2)

            # Atualizar texto com os ângulos detectados
            angles_text.value = f"Ângulos: Direito = {right_arm_angle}"
            page.update()

        # Converter img (BGR) para formato aceito pelo Flet
        ret, jpeg = cv2.imencode(".jpg", img)
        video_player.content = ft.UserContentBytes(jpeg.tobytes())
        page.update()

        # Repetir após um curto atraso
        page.delay(100, update_frame)

    # Iniciar atualização de frame
    update_frame()


def page(page: ft.Page):
    t = ft.Text(
        value="This is a test",
        size=20,
    )
    page.controls.append(t)
    page.update()


if __name__ == "__main__":

    ft.app(target=page)
