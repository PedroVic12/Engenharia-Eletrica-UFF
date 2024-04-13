import easygui
import sympy as sp
import scipy
from IPython import display


class Calculator:
    def __init__(self):
        pass

    def get(self):
        x, y, z = sp.symbols("x y z")
        return x, y, z

    def f_x0(self, f, x):
        """sympy finds the value of  that makes f(x) = 0"""
        solutions = sp.solve(f, x)
        print(f"Solução de {f} em {x}, sendo x = 0")
        print(solutions)

    def convert_to_symbol(self, expression):
        try:
            expr = sp.sympify(expression)

            return expr
        except Exception as e:
            return None, f"Erro ao converter para símbolos: {e}"

    def integrate(self, expr, var):
        try:
            if expr:
                integral = sp.integrate(expr, var)
                return integral
            else:
                return None, "Expressão inválida"
        except Exception as e:
            return None, f"Erro ao integrar: {e}"

    def differentiate(self, expr, variable):
        try:
            if expr:
                derivative = sp.diff(expr, variable)
                print(f"Derivada entre de {expr} em {variable}")
                return derivative
            else:
                return None, "Expressão inválida"
        except Exception as e:
            return None, f"Erro ao diferenciar: {e}"


class MatrixCalculator:
    def __init__(self) -> None:
        self.calculadora = Calculator()

    def produto_vetorial(self, u, v):
        print(f"produto vetorial entre {u} x {v}")
        return u.dot(v)

    def cross(self, u, v):
        u.cross(v)

    def normalizar_vetor(self, u):
        u.norm()


def main_calculadora():
    calculator = Calculator()

    msg = "Digite a função:"
    title = "Calculadora"
    expression = easygui.enterbox(msg, title)

    if expression:
        symbol_expr, error = calculator.convert_to_symbol(expression)
        if symbol_expr:
            msg = "Selecione a operação:"
            choices = ["Integrar", "Diferenciar"]
            operation = easygui.buttonbox(msg, title, choices=choices)

            if operation == "Integrar":
                variable = easygui.enterbox("Digite a variável de integração:")
                integral_result, error = calculator.integrate(expression, variable)
                if integral_result:
                    easygui.msgbox(f"Resultado da integração:\n{integral_result}")
                else:
                    easygui.msgbox(error, "Erro")

            elif operation == "Diferenciar":
                variable = easygui.enterbox("Digite a variável de diferenciação:")
                derivative_result, error = calculator.differentiate(
                    expression, variable
                )
                if derivative_result:
                    easygui.msgbox(f"Resultado da diferenciação:\n{derivative_result}")
                else:
                    easygui.msgbox(error, "Erro")
        else:
            easygui.msgbox(error, "Erro")
