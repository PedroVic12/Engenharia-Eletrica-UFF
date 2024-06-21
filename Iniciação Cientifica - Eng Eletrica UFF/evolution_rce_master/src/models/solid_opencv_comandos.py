import cv2
import cvzone


class WebCam:
    def __init__(self) -> None:

        pass

    def desenha_retangulo(self, imagem):

        cvzone.cornerRect(
            imagem,
            (200, 200, 300, 200),
            l=100,
            t=5,
            rt=1,
            colorR=(255, 0, 255),
            colorC=(255, 0, 0),
        )
        cv2.exibe_imagem("Imagem", imagem)

    def exibe_imagem(self, imagem):
        cv2.imshow("WebCam", imagem)

    #!LOOP
    def main_loop(self):

        caputa = cv2.VideoCapture(0)
        while True:
            sucesso, imagem = caputa.read()

            # todo fazer acontecer
            # coordenadas = [(200, 200), (500, 400), (255, 0, 255), 3]
            # cv2.rectangle(imagem, (200, 200), (500, 400), (255, 0, 255), 3)
            # self.desenha_retangulo(imagem)

            cvzone.cornerRect(imagem, (200, 200, 300, 200))

            self.exibe_imagem(imagem)
            # desliga
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        caputa.release()
        cv2.destroyAllWindows()
        print(
            "Camera released"
        )  # print a message to let us know the camera has been released


def main_webcam():
    cam = WebCam()
    cam.main_loop()


main_webcam()
