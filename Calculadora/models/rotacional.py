import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definindo variáveis simbólicas
x, y, z = sp.symbols("x y z")

# Definindo a função vetorial
F = sp.Matrix([x**2 * y, y**2 * z, z**2 * x])

# Calculando o rotacional
rot_F = sp.curl(F, (x, y, z))

# Função para avaliar as expressões
evaluate_rot = sp.lambdify((x, y, z), rot_F, "numpy")

# Definindo intervalo para avaliação
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
z_vals = np.linspace(-5, 5, 20)

# Avaliando o rotacional em todos os pontos do intervalo
rot_F_vals = evaluate_rot(x_vals, y_vals, z_vals)

# Plotando o rotacional em 2D
plt.figure(figsize=(8, 6))
plt.quiver(x_vals, y_vals, rot_F_vals[0], rot_F_vals[1], scale=20)
plt.title("Rotacional em 2D")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# Plotando o rotacional em 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.quiver(
    x_vals, y_vals, z_vals, rot_F_vals[0], rot_F_vals[1], rot_F_vals[2], length=0.5
)
ax.set_title("Rotacional em 3D")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
