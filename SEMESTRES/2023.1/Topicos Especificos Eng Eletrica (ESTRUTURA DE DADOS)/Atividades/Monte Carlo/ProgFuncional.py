import math
import random


def monte_carlo_simulation(f, D, beta_threshold):
    stack = []
    stack.append((0, 0, 0))  # (N, sigma, sigma_squared)

    def iteration(state):
        N, sigma, sigma_squared = state

        N += 1
        x = random.choices(list(f.keys()), list(f.values()))[0]
        D_x = D(x)

        sigma += D_x
        sigma_squared += D_x ** 2

        return N, sigma, sigma_squared

    while stack:
        state = stack.pop()

        N, sigma, sigma_squared = iteration(state)

        if N > 1:
            l = sigma / N
            variance = (sigma_squared / N) - (l ** 2)
            s = math.sqrt(variance)
            beta = (s / l) / math.sqrt(N)

            if beta < beta_threshold:
                return l, s, beta

        stack.append((N, sigma, sigma_squared))


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

l, s, beta = monte_carlo_simulation(f, D, beta_threshold)

print("Valor esperado (l):", l)
print("Desvio padrão (s):", s)
print("Parâmetro beta (β):", beta)
