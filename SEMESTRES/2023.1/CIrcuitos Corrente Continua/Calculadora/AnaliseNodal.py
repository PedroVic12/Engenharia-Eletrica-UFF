import numpy as np


class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def inverter_matriz(self):
        if len(self.matriz) != len(self.matriz[0]):
            raise ValueError(
                "A matriz precisa ser quadrada para ser invertida.")

        n = len(self.matriz)
        matriz = np.array(self.matriz)

        matriz_concatenada = np.concatenate((matriz, np.identity(n)), axis=1)

        for i in range(n):
            pivot = matriz_concatenada[i, i]
            if pivot == 0:
                raise ValueError("A matriz não pode ser invertida.")

            # Dividindo a linha atual pelo pivô para tornar o pivô igual a 1
            matriz_concatenada[i, :] /= pivot

            for k in range(n):
                if k != i:
                    fator = matriz_concatenada[k, i]
                    # Subtraindo múltiplos da linha atual das outras linhas
                    matriz_concatenada[k, :] -= fator * \
                        matriz_concatenada[i, :]

        inversa = matriz_concatenada[:, n:]

        return Matriz(inversa.tolist())

    def multiplicar_matriz(self, outra_matriz):
        if len(self.matriz[0]) != len(outra_matriz.matriz):
            raise ValueError(
                "As dimensões das matrizes são incompatíveis para a multiplicação.")

        resultado = np.dot(np.array(self.matriz),
                           np.array(outra_matriz.matriz))

        return Matriz(resultado.tolist())


matriz_nodal = Matriz(
    [
        [-(1/2+1/2+1/5), 1/2, 1/5, 1/2, 0],
        [1/2, -(1/4+1/2+1/2), 1/2, 0, 0],
        [1/5, 1/2, -(1/5+1/3+1/2), 0, 0],
        [1/2, 0, 0, -(1/4+1/2+1), 1],
        [0, 0, 0, 1, -(1+1/3+1)]
    ]
)

matriz_termoIndependente = Matriz(
    [
        [-7],
        [-1/2],
        [-4],
        [5],
        [-6]
    ]
)

matriz_inversa = matriz_nodal.inverter_matriz()
resultado = matriz_inversa.multiplicar_matriz(matriz_termoIndependente)

va = resultado.matriz[0][0]
vb = resultado.matriz[1][0]
vc = resultado.matriz[2][0]
vd = resultado.matriz[3][0]
ve = resultado.matriz[4][0]

print(f"va = {va:.2f} V")
print(f"vb = {vb:.2f} V")
print(f"vc = {vc:.2f} V")
print(f"vd = {vd:.2f} V")
print(f"ve = {ve:.2f} V")
