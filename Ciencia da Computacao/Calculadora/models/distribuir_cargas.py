import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate


class DistribuicaoCargas:
    def __init__(self, x_centro, y_centro, z_centro, raio):
        self.x_centro = x_centro
        self.y_centro = y_centro
        self.z_centro = z_centro
        self.raio = raio

    def potencial_eletrostatico(self, x, y, z):
        # Calcular a distância entre o ponto (x, y, z) e o centro da distribuição de cargas
        distancia = np.sqrt(
            (x - self.x_centro) ** 2
            + (y - self.y_centro) ** 2
            + (z - self.z_centro) ** 2
        )

        # Se a distância for zero, retornar NaN para evitar divisão por zero
        if distancia == 0:
            return np.nan

        # Calcular o potencial elétrico usando a fórmula do potencial de uma carga puntiforme
        k = 8.9875517923 * 10**9  # Constante de Coulomb
        potencial = k / distancia

        return potencial

    def plot_potencial_volume(self):
        # Definir intervalos de coordenadas para o volume
        x = np.linspace(self.x_centro - self.raio, self.x_centro + self.raio, 50)
        y = np.linspace(self.y_centro - self.raio, self.y_centro + self.raio, 50)
        z = np.linspace(self.z_centro - self.raio, self.z_centro + self.raio, 50)

        # Criar uma grade de coordenadas tridimensionais
        X, Y, Z = np.meshgrid(x, y, z)

        # Calcular o potencial elétrico para cada ponto na grade
        potencial = np.zeros_like(X)
        for i in range(len(x)):
            for j in range(len(y)):
                for k in range(len(z)):
                    potencial[i, j, k] = self.potencial_eletrostatico(
                        X[i, j, k], Y[i, j, k], Z[i, j, k]
                    )

        # Plotar o volume da distribuição de cargas com cores representando o potencial elétrico
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(X, Y, Z, c=potencial.flatten(), cmap="viridis")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Volume da Distribuição de Cargas com Potencial Elétrico")
        plt.colorbar(
            ax.scatter(X, Y, Z, c=potencial.flatten(), cmap="viridis"),
            label="Potencial Elétrico (V)",
        )
        plt.show()


# Exemplo de uso
distribuicao_cargas = DistribuicaoCargas(x_centro=0, y_centro=0, z_centro=0, raio=1)
distribuicao_cargas.plot_potencial_volume()
