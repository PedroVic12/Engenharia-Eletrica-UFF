from scipy.signal import convolve
import numpy as np
import matplotlib.pyplot as plt

# Sinais de exemplo
x = np.array([1, 2, 3])
h = np.array([0.5, 1, 0.5])

# Realizar a convolução
y = convolve(x, h, mode='full')

# Plotar os sinais e o resultado da convolução
plt.stem(x, basefmt=" ", linefmt="b-", markerfmt="bo", label='x[n]')
plt.stem(h, linefmt="g-", markerfmt="go", label='h[n]')
plt.stem(y, linefmt="r-", markerfmt="ro", label='x[n] * h[n]')
plt.legend()
plt.show()
