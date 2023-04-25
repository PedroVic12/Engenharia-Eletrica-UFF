import math


def derivada(f, x, h=1e-8):
    res = (f(x + h) - f(x)) / h
    return res


g = math.sin
y = math.pi
print('Resultado = ', derivada(g, 0))
print('Resultado = ', derivada(g, y))

# print('dg_dy' = '{}')
