import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class PotencialEletrostatico3D:
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi

    def calcular_coordenadas_cartesianas(self):
        x = self.r * np.sin(self.phi) * np.cos(self.theta)
        y = self.r * np.sin(self.phi) * np.sin(self.theta)
        z = self.r * np.cos(self.phi)
        return x, y, z

    def plot_potencial_eletrostatico(self):
        x, y, z = self.calcular_coordenadas_cartesianas()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x, y, z, c="r", marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Potencial Eletrostático em Coordenadas Esféricas")
        plt.show()


# Exemplo de uso
r = 1.0  # raio
theta = np.pi / 4  # ângulo azimutal
phi = np.pi / 4  # ângulo polar

potencial = PotencialEletrostatico3D(r, theta, phi)
potencial.plot_potencial_eletrostatico()
