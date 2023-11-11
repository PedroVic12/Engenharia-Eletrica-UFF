from scipy.signal import get_window
import matplotlib.pyplot as plt

# Escolher uma janela (por exemplo, janela de Hamming)
window = get_window('hamming', 64)

# Plotar a janela
plt.plot(window)
plt.title('Janela de Hamming')
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
