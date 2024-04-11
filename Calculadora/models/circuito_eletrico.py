import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class Circuit:
    def __init__(self, resistance1, resistance2, voltage_source):
        self.R1 = resistance1
        self.R2 = resistance2
        self.V = voltage_source
        # Definir símbolos para as correntes nos resistores
        self.I1, self.I2 = sp.symbols('I1 I2')

    def circuit_equations(self):
        # Equações diferenciais que representam as correntes nos resistores
        eq1 = (self.V - self.R1 * self.I1 - self.R2 * (self.I1 - self.I2)) / self.R1
        eq2 = (self.R1 * (self.I1 - self.I2) - self.R2 * self.I2) / self.R2
        return [eq1, eq2]

    def solve_circuit(self):
        # Resolver o sistema de equações diferenciais simbolicamente
        solution = sp.solve(self.circuit_equations(), (self.I1, self.I2))
        return solution

    def plot_response(self, solution):
        # Extrair as soluções para as correntes nos resistores
        I1_solution = solution[self.I1]
        I2_solution = solution[self.I2]

        # Converter as expressões simbólicas em funções numpy
        I1_func = sp.lambdify((), I1_solution, 'numpy')
        I2_func = sp.lambdify((), I2_solution, 'numpy')

        # Definir o intervalo de tempo
        t = np.linspace(0, 10, 100)

        # Calcular as correntes nos resistores ao longo do tempo
        currents_R1 = I1_func()
        currents_R2 = I2_func()

        # Plotar a resposta do circuito
        plt.plot(t, currents_R1, label='Corrente no Resistor R1')
        plt.plot(t, currents_R2, label='Corrente no Resistor R2')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Corrente (A)')
        plt.title('Resposta do Circuito')
        plt.legend()
        plt.grid(True)
        plt.show()

# Parâmetros do circuito
resistance1 = 100  # Resistência R1 em ohms
resistance2 = 200  # Resistência R2 em ohms
voltage_source = 10  # Tensão da fonte de tensão em volts

# Criar objeto do circuito
circuit = Circuit(resistance1, resistance2, voltage_source)

# Resolver o circuito simbolicamente
solution = circuit.solve_circuit()

# Plotar a resposta do circuito
circuit.plot_response(solution)
