from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt

# Parâmetros do filtro FIR
num_taps = 64
cutoff_freq = 0.1

# Projeto da janela do filtro
fir_coefficients = firwin(num_taps, cutoff_freq)

# Resposta em frequência do filtro
w, h = freqz(fir_coefficients)

# Plotar a resposta em frequência
plt.plot(w, abs(h))
plt.title("Resposta em Frequência do Filtro FIR")
plt.xlabel("Frequência normalizada")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
