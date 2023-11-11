from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Criar um sinal de exemplo
t = np.linspace(0, 1, 1000, endpoint=False)
signal_freq = 5  # Frequência do sinal
signal_amplitude = 1
signal_waveform = signal_amplitude * np.sin(2 * np.pi * signal_freq * t)

# Criar um filtro FIR passa-baixa
cutoff_freq = 10  # Frequência de corte
num_taps = 30
fir_filter = signal.firwin(num_taps, cutoff_freq / (0.5 * 1000))

# Aplicar o filtro ao sinal
filtered_signal = signal.lfilter(fir_filter, 1.0, signal_waveform)

# Plotar o sinal original e o sinal filtrado
plt.plot(t, signal_waveform, label='Sinal Original')
plt.plot(t, filtered_signal, label='Sinal Filtrado')
plt.legend()
plt.show()
