import math
import random


class MonteCarloSimulation:
    def __init__(self, f, D, beta_threshold):
        self.f = f
        self.D = D
        self.beta_threshold = beta_threshold
        self.N = 0
        self.sum_D = 0
        self.sum_D_squared = 0

    def run(self):
        while True:
            self.N += 1
            x = random.choices(list(self.f.keys()), list(self.f.values()))[0]
            D_x = self.D(x)

            self.sum_D += D_x
            self.sum_D_squared += D_x ** 2

            if self.N > 1:
                l = self.sum_D / self.N
                variance = (self.sum_D_squared / self.N) - (l ** 2)
                s = math.sqrt(variance)
                beta = (s / l) / math.sqrt(self.N)

                if beta < self.beta_threshold:
                    break

        return l, s, beta


# Exemplo de uso
# Função de distribuição de probabilidade
f = {
    1: 0.3,
    2: 0.5,
    3: 0.2
}

# Função de desempenho


def D(x):
    return x ** 2


# Parâmetro de tolerância
beta_threshold = 0.01

simulation = MonteCarloSimulation(f, D, beta_threshold)
l, s, beta = simulation.run()

print("Valor esperado (l):", l)
print("Desvio padrão (s):", s)
print("Parâmetro beta (β):", beta)
