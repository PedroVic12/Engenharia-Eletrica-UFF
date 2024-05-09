import numpy as np
import math
from deap import base, creator, tools
import random
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import pandas as pd
import json
from typing import List, Callable, Optional


class CustomIndividual(list):
    def __init__(
        self,
        tipo: str,
        quantidade_var_decision: int,
        limite_var: List[Optional[float]],
        *args
    ):
        super().__init__(*args)
        self.tipo = tipo
        self.quantidade_var_decision = quantidade_var_decision
        self.limite_var = limite_var
        self.index = None
        self.rce = None
        self.Fitness = None


class SetupRCE:
    def __init__(
        self,
        params,
    ):

        #! Parametros JSON
        self.params = params

        self.CXPB = params["CROSSOVER"]
        self.MUTPB = params["MUTACAO"]
        self.NGEN = params["NUM_GENERATIONS"]
        self.POP_SIZE = params["POP_SIZE"]
        self.SIZE_INDIVIDUAL = params["IND_SIZE"]
        self.TAXA_GENERATION = params["RCE_REPOPULATION_GENERATIONS"]
        self.CROSSOVER, self.MUTACAO, self.NUM_GENERATIONS, self.POPULATION_SIZE = (
            self.CXPB,
            self.MUTPB,
            self.NGEN,
            self.POP_SIZE,
        )

        self.delta = params["DELTA"]
        self.rce_evaluations = params["RCE_REPOPULATION_GENERATIONS"]
        self.porcentagem = params["PORCENTAGEM"]
        self.bestInd = tools.HallOfFame(1)

        #! Parâmetros do algoritmo de Rastrigin
        self.evaluations = 0
        self.num_repopulation = int(self.NUM_GENERATIONS * self.TAXA_GENERATION)
        self.type = params["type"].lower()
        if self.type == "maximize":
            creator.create("Fitness", base.Fitness, weights=(1.0,))
        else:
            creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

        self.dataset = {}

        #!Criando individuo pelo deap com seus atributos
        self.toolbox = base.Toolbox()

    # Exemplo de configuração do DEAP
    def configure_deap(
        self,
        tipo: str,
        quantidade_var_decision: int,
        limite_var: List[Optional[float]],
        fitness_function=None,
    ):
        creator.create("Fitness", base.Fitness, weights=(-1.0,))
        creator.create(
            "Individual",
            CustomIndividual,
            fitness=creator.Fitness,
            rce=str,
            index=int,
        )

        # Registro de parâmetros evolutvos
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        # Registro de função para inicializar os atributos dos indivíduos
        if tipo == "int":
            self.toolbox.register(
                "attribute", random.randint, limite_var[0], limite_var[1]
            )
        elif tipo == "float":
            self.toolbox.register(
                "attribute", random.uniform, limite_var[0], limite_var[1]
            )
        elif tipo == "binario":
            self.toolbox.register("attribute", random.randint, 0, 1)
        else:
            raise ValueError("Tipo de variável inválido")

        # Registro da função de avaliação (fitness)
        if fitness_function is not None:
            self.toolbox.register("evaluate", fitness_function)
        else:
            self.toolbox.register("evaluate", self.rastrigin_fitness)
            # self.toolbox.register("evaluate", self.evaluate_fitness)

        # Função para criar um indivíduo com atributos personalizados
        def create_individual(
            tipo: str,
            quantidade_var_decision: int,
            limite_var: List[Optional[float]],
        ):
            individual = creator.Individual(
                tipo,
                quantidade_var_decision,
                limite_var,
                [self.toolbox.attribute() for _ in range(quantidade_var_decision)],
            )
            individual.tipo = tipo
            individual.quantidade_var_decision = quantidade_var_decision
            individual.limite_var = limite_var
            individual.Fitness = (
                fitness_function if fitness_function else self.rastrigin
            )
            return individual

        # Registro da função de criação de indivíduos
        self.toolbox.register(
            "individual",
            create_individual,
            tipo,
            quantidade_var_decision,
            limite_var,
        )

        #! paramentos evolutivos
        self.toolbox.register(
            "population", tools.initRepeat, list, self.toolbox.individual
        )

        return self.toolbox

    def evaluate_fitness(self, individual):
        if self.type == "minimaze":
            result = minimize(
                self.rastrigin, x0=np.zeros(self.SIZE_INDIVIDUAL), method="BFGS"
            )
            fitness_value = result.fun
        return fitness_value

    def gerarDataset(self, excel):
        df = pd.read_excel(excel)
        print(df.columns)
        self.dataset = {
            "CXPB": self.CROSSOVER,
            "TAXA_MUTACAO": self.MUTACAO,
            "NUM_GEN": self.NUM_GENERATIONS,
            "POP_SIZE": self.POPULATION_SIZE,
            "IND_SIZE": self.SIZE_INDIVIDUAL,
            "evaluations": self.evaluations,
            "NUM_REPOPULATION": self.num_repopulation,
        }

    def rastrigin(self, individual):
        self.evaluations += 1
        rastrigin = 10 * self.SIZE_INDIVIDUAL
        for i in range(self.SIZE_INDIVIDUAL):
            rastrigin += individual[i] * individual[i] - 10 * (
                math.cos(2 * np.pi * individual[i])
            )
        return rastrigin

    def rastrigin_fitness(self, individual: CustomIndividual) -> float:
        rastrigin = 10 * len(individual)
        for i in range(len(individual)):
            rastrigin += individual[i] ** 2 - 10 * (np.cos(2 * np.pi * individual[i]))
        return (rastrigin,)

    def rosenbrock(self, x):
        return np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)

    def rastrigin_decisionVariables(self, individual, decision_variables):
        self.evaluations += 1
        rastrigin = 10 * len(decision_variables)
        for i in range(len(decision_variables)):
            rastrigin += individual[i] * individual[i] - 10 * (
                math.cos(2 * np.pi * individual[i])
            )
        return rastrigin

    def globalSolutions(self):
        n_dimensions = 2

        try:
            rastrigin_result = minimize(
                self.rastrigin, x0=np.zeros(n_dimensions), method="BFGS"
            )
            rastrigin_minimum = rastrigin_result.fun
            rastrigin_solution = rastrigin_result.x

            rosenbrock_result = minimize(
                self.rosenbrock, x0=np.zeros(n_dimensions), method="BFGS"
            )
            rosenbrock_minimum = rosenbrock_result.fun
            rosenbrock_solution = rosenbrock_result.x

        except Exception as e:
            print("Erro ao tentar encontrar o ótimo global das funções: ", e)

        print("\n\nÓtimo global da função Rastrigin: ", rastrigin_minimum)
        print("Solução: ", rastrigin_solution)
        print()
        print("Ótimo global da função Rosenbrock: ", rosenbrock_minimum)
        print("Solução: ", rosenbrock_solution)


def load_params(file_path):
    with open(file_path, "r") as file:
        params = json.load(file)
    return params


def customFitness(individual):
    return sum(individual) ** 2


def main_setup():
    #! Setup
    params = load_params(
        r"/home/pedrov/Documentos/GitHub/Engenharia-Eletrica-UFF/Iniciação Cientifica - Eng Eletrica UFF/evolution_rce_master/src/db/parameters.json"
    )
    setup = SetupRCE(params)

    def avaliarFitnessIndividuos(pop):
        """Avaliar o fitness dos indivíduos da população atual."""
        fitnesses = map(setup.toolbox.evaluate, pop)
        for ind, fit in zip(pop, fitnesses):
            if ind.fitness.values:
                ind.fitness.values = [fit]

    #! Exemplo de uso
    tipo = "int"  # Pode ser "int", "float" ou "binario"
    quantidade_var_decision = 5
    limite_var = [-5, 5]

    my_toolbox = setup.configure_deap(tipo, quantidade_var_decision, limite_var)

    #! Criação de um indivíduo
    ind = my_toolbox.individual()
    fitness = my_toolbox.evaluate(ind)

    print("\n\n", type(ind))

    print("Indivíduo:", ind)
    print("Tipo:", ind.tipo)
    print("Quantidade de Variáveis de Decisão:", ind.quantidade_var_decision)
    print("Limites Variáveis:", ind.limite_var)
    print("Índice:", ind.index)  # Pode ser None
    print("RCE:", ind.rce)  # Pode ser None

    # Avaliação do indivíduo usando a função Rastrigin
    print("Fitness do Indivíduo:", fitness)

    newPop = my_toolbox.population(n=5)
    print("\nPopulação gerada\n", newPop)
    avaliarFitnessIndividuos(newPop)

    for i, ind in enumerate(newPop):
        ind.Fitness = my_toolbox.evaluate(ind)
        ind.fitness = my_toolbox.evaluate(ind)
        ind.index = i + 1
        print("\n")
        print(ind.index, ind)
        print(ind.fitness)

    setup.bestInd.update(newPop)
    newPop[0] = setup.toolbox.clone(setup.bestInd[0])
    print("Best Da geração= ", newPop[0], newPop[0].Fitness[0])


main_setup()
