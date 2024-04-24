# from Calculadora import Calculadora
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from scipy.optimize import fsolve
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D


# from Calculadora import Calculadora


class EletroMagnetismo:
    def __init__(self):
        pass

    def plot_campo(self, values, campo="gravitacional"):
        x, y = np.meshgrid(np.linspace(-1.5, 1.5, 15), np.linspace(-1.5, 1.5, 15))

        if campo == "gravitacional":
            vx, vy = self.campoGravitacional(values[0], values[1], x, y)
            plt.quiver(x, y, vx, vy)
        elif campo == "eletrico":
            vx, vy = self.campoEletrico(values[2], values[0], values[1], x, y)
            plt.streamplot(x, y, vx, vy)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def campoEletrico(self, q, x0, y0, x, y, k=8.9875e9):
        vx = x - x0
        vy = y - y0

        d = np.sqrt(vx**2 + vy**2)

        v = np.array([vx, vy])

        vu = v / d

        E = k * q * vu / d**2

        return E[0], E[1]

    def campoGravitacional(self, x0, y0, x, y, k=1):
        vx = x0 - x
        vy = y0 - y

        d = np.sqrt(vx**2 + vy**2)

        v = np.array([vx, vy])

        vu = v / d

        f = k * vu / d**2

        return f[0], f[1]

    def plot_vetor(self, x, y, vx, vy, _tamanho, _label):
        fig = ff.create_quiver(
            x,
            y,
            vx,
            vy,
            scale=0.1,
            arrow_scale=_tamanho,
            name=_label,
            line_width=2,
            marker=dict(color="red"),
        )
        fig.add_trace(
            go.Scatter(
                x=[0],
                y=[0],
                mode="markers",
                marker=dict(color="black"),
                marker_size=12,
                name=" Origem",
            )
        )
        fig.show()

    def plot_campoMagnetico(self, values=[0, 0]):
        x, y = np.meshgrid(np.linspace(-1.5, 1.5, 15), np.linspace(-1.5, 1.5, 15))

        vx, vy = self.campoGravitacional(values[0], values[1], x, y)
        # fig, ax = plt.subplots
        plt.figure(figsize=(10, 10))
        # plt.streamplot(x,y,vx,vy)
        plt.quiver(x, y, vx, vy)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def plot_campoVetorial(self):
        x, y = np.meshgrid(np.linspace(-1.5, 1.5, 15), np.linspace(-1.5, 1.5, 15))

        vx, vy = self.campoGravitacional(0, 0, x, y)
        # fig, ax = plt.subplots
        plt.figure(figsize=(10, 10))
        plt.streamplot(x, y, vx, vy)

    def calcular_vetor_posicao(self, x0, y0, z0, x, y, z):
        """Calcula o vetor posição entre dois pontos."""
        vetor_posicao = np.array([x - x0, y - y0, z - z0])
        return vetor_posicao

    def plotar_pontos_3d(self, coordenadas):
        """Plota os pontos no espaço tridimensional."""
        fig = go.Figure()

        for i, (x, y, z) in enumerate(coordenadas, start=1):
            nome_carga = f"q{i}"
            cor = f"rgb({30 * i}, {50 * i}, {70 * i})"
            fig.add_trace(
                go.Scatter3d(
                    x=[x],
                    y=[y],
                    z=[z],
                    mode="markers",
                    name=nome_carga,
                    marker=dict(size=10, color=cor),
                    text=nome_carga,
                )
            )

        fig.update_layout(
            scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
            title="Localização das Cargas",
        )
        fig.show()

    def calcular_forca_electrica(q1, q2, x1, y1, z1, x2, y2, z2):
        """Calcula a força elétrica entre duas cargas."""
        k = 8.99e9  # Constante eletrostática em N.m^2/C^2

        # Calcula a distância entre as cargas
        r = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

        # Calcula o vetor posição
        r_vec = np.array([x2 - x1, y2 - y1, z2 - z1])

        # Calcula a força elétrica
        F = k * (q1 * q2) / r**2

        # Calcula o vetor força
        F_vec = (F * r_vec) / r

        return F_vec

    def plotar_cargas_eletricas(self, coordenadas, q1, q2):
        """Plota os vetores força no espaço tridimensional."""
        fig = go.Figure()

        for i, (x, y, z) in enumerate(coordenadas, start=1):
            nome_carga = f"q{i}"
            cor = f"rgb({30 * i}, {50 * i}, {70 * i})"
            fig.add_trace(
                go.Scatter3d(
                    x=[x],
                    y=[y],
                    z=[z],
                    mode="markers",
                    name=nome_carga,
                    marker=dict(size=10, color=cor),
                    text=nome_carga,
                )
            )

        for i, (x, y, z) in enumerate(coordenadas[1:], start=1):
            F_vec = calcular_forca_electrica(
                q1, q2, coordenadas[0][0], coordenadas[0][1], coordenadas[0][2], x, y, z
            )
            fig.add_trace(
                go.Scatter3d(
                    x=[coordenadas[0][0], coordenadas[0][0] + F_vec[0]],
                    y=[coordenadas[0][1], coordenadas[0][1] + F_vec[1]],
                    z=[coordenadas[0][2], coordenadas[0][2] + F_vec[2]],
                    mode="lines",
                    name=f"F{3}{i}",
                    marker=dict(size=2),
                    line=dict(color=f"rgb({255 * i}, {100 * i}, {50 * i})"),
                )
            )

        fig.update_layout(
            scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
            title="Forças Elétricas",
        )
        fig.show()
