import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmin, argrelmax, argrelextrema

data, timer = hp.load_exampledata(1)
print(data)

#Encontrandos os mnimos e maximos relativos
min_indices = argrelmin(data)[0]
max_indices = argrelmax(data)[0]

#Encontrando ambos os extremos
extreme_indices = argrelextrema(data, np.greater)[0]

#visualização
plt.figure(figsize=(12,4))
plt.plot(data, label = 'Sinal PPG', color = 'gray')
plt.scatter(min_indices,data[min_indices], color = 'blue', label = 'Mínimos Relativos')
plt.scatter(max_indices,data[max_indices], color = 'red', label = 'Maximos Relativos')
plt.scatter(extreme_indices, data[extreme_indices], color = 'green', s =10, label = 'Extremos')
plt.legend()
plt.title('Analise de minimos e maximos relativos do Sinal')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()

