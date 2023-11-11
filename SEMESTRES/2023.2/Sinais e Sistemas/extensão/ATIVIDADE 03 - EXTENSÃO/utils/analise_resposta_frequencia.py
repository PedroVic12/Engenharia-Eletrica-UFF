from scipy.signal import freqz
import matplotlib.pyplot as plt

# Parâmetros do filtro
b = [0.1, 0.2, 0.3, 0.4, 0.5]
a = [1, -0.5, 0.25, -0.125, 0.0625]

# Calcular a resposta em frequência
w, h = freqz(b, a)

# Plotar a resposta em frequência
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Resposta em Frequência')
plt.xlabel('Frequência [radianos / amostra]')
plt.ylabel('Ganho [dB]')
plt.grid()
plt.show()
