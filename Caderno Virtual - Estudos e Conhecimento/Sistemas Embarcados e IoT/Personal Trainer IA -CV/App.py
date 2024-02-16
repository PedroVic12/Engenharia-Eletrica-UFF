import cv2
import tkinter as tk
from tkinter import ttk
import PIL.Image, PIL.ImageTk
import numpy as np
import pandas as pd
from src.models.poseModule import poseDetector

# Supondo que detector seja inicializado aqui


class Application:
    def __init__(
        self,
        window,
        window_title,
        video_source="Personal Trainer IA -CV/assets/flexao_normal.mp4",
    ):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Abre o vídeo de origem
        self.vid = cv2.VideoCapture(video_source)

        # Cria um canvas que pode caber a resolução do vídeo.
        self.canvas = tk.Canvas(
            window,
            width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
            height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT),
        )
        self.canvas.pack()

        # Cria um label para mostrar os ângulos
        self.label = ttk.Label(window, text="Ângulos:")
        self.label.pack(anchor=tk.CENTER, expand=True)

        # Botão que permite iniciar o processamento do vídeo
        self.btn_snapshot = tk.Button(
            window, text="Iniciar", width=50, command=self.process_video
        )
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15  # ms
        self.window.mainloop()

    def process_video(self):
        # Pega um frame do vídeo
        ret, frame = self.vid.read()
        if ret:
            # Processa o frame
            frame = detector.findPose(frame, draw=True)
            lmList = detector.findPosition(frame, draw=False)

            # Atualiza a interface gráfica com os novos dados
            if len(lmList) != 0:
                right_arm_angle = round(detector.findAngle(frame, 12, 14, 16), 2)
                left_arm_angle = round(detector.findAngle(frame, 11, 13, 15), 2)
                self.label.config(
                    text=f"Ângulos: Direito = {right_arm_angle}, Esquerdo = {left_arm_angle}"
                )

            # Converte o frame do BGR para RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.process_video)  # Repete após 'delay' ms


# Cria uma janela e passa a instância do detector e o caminho do vídeo
detector = poseDetector()
app = Application(tk.Tk(), "Tkinter e OpenCV")
