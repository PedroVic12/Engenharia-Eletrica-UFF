import numpy as np

# Define a posição e a carga das partículas
charge1_pos = np.array([1, 0, 0])  # posição da carga 1 em metros
charge1_q = 1e-6  # carga da carga 1 em Coulombs

charge2_pos = np.array([-1, 0, 0])  # posição da carga 2 em metros
charge2_q = -1e-6  # carga da carga 2 em Coulombs

# Define a posição onde queremos calcular o potencial elétrico
point_pos = np.array(
    [0, 1, 0]
)  # posição do ponto onde queremos calcular o potencial em metros

# Calcula a distância entre as cargas e o ponto
dist1 = np.linalg.norm(point_pos - charge1_pos)
dist2 = np.linalg.norm(point_pos - charge2_pos)

# Calcula o potencial elétrico de cada carga no ponto
V1 = 9e9 * charge1_q / dist1
V2 = 9e9 * charge2_q / dist2

# Soma os potenciais elétricos das duas cargas
V_total = V1 + V2

print("Potencial elétrico total em coordenadas cartesianas:", V_total, "V")
