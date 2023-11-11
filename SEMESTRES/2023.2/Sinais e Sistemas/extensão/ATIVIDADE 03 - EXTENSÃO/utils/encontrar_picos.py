from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Criar um sinal de exemplo com picos
x = np.linspace(0, 2 * np.pi, 100)
signal = np.sin(x)

# Encontrar picos no sinal
peaks, _ = find_peaks(signal)

# Plotar o sinal com os picos destacados
plt.plot(x, signal)
plt.plot(x[peaks], signal[peaks], "x")
plt.show()
