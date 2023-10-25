from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

# Criar um sinal de exemplo
t = np.linspace(0, 1, 1000, endpoint=False)
signal_freq = 5  # Frequência do sinal
signal_amplitude = 1
signal_waveform = signal_amplitude * np.sin(2 * np.pi * signal_freq * t)

# Calcular a transformada de Fourier
signal_spectrum = fft(signal_waveform)

# Plotar o espectro de frequência
plt.plot(np.abs(signal_spectrum))
plt.show()
