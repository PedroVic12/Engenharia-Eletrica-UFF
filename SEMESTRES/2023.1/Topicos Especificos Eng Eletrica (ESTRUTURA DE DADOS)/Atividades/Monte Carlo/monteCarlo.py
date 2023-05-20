import math
import random


def monte_carlo_simulation(f, D, beta_threshold, Nmax):
    N = 0
    sigma = 0
    sigma_squared = 0

    while N < Nmax:
        N += 1
        x = random.choices(list(f.keys()), list(f.values()))[0]
        D_x = D(x)

        sigma += D_x
        sigma_squared += D_x ** 2

    l = sigma / Nmax
    variance = (sigma_squared / Nmax) - (l ** 2)
    s = math.sqrt(variance)
    beta = (s / l) / math.sqrt(Nmax)

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

# Número máximo de amostras
Nmax = int(input("Digite o número máximo de amostras: "))

l, s, beta = monte_carlo_simulation(f, D, beta_threshold, Nmax)

print("Valor esperado (l):", l)
print("Desvio padrão (s):", s)
print("Parâmetro beta (β):", beta)
