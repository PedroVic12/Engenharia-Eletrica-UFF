import random
from deap import base, creator, tools
import numpy as np
from faker import Faker

fake = Faker()


# Define a classe personalizada para o indivíduo
class MeuIndividuo:
    def __init__(self, genes):
        self.genes = genes
        self.nome = fake.name()

    def __str__(self):
        return (
            "Individuo = {self.nome} Genes: "
            + str(self.genes)
            + ", Fitness: "
            + str(self.fitness)
        )


# Define o tipo Fitness e Indivíduo
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Configuração do toolbox
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register(
    "individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10
)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# Definição da função de avaliação
def evaluateInd(individual):
    return (sum(individual),)  # A função de avaliação simplesmente soma os genes


def rastrigin(individual):
    A = 10
    n = len(individual)
    return (A * n + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in individual]),)


toolbox.register("evaluate", rastrigin)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    population = toolbox.population(n=200)
    CXPB, MUTPB, NGEN = 0.9, 0.05, 5

    # Avalia a população inicial
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    # Evolução
    for g in range(NGEN):
        print(f"\n--- Geração {g+1} ---")

        # Seleciona os próximos indivíduos para a próxima geração
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Aplica cruzamento e mutação
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Avalia os indivíduos com fitness inválido
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        population[:] = offspring

        # Imprime a população
        for ind_num, ind in enumerate(population):
            print(f"Indivíduo {ind_num}:  Genes:{ind}, Fitness: {ind.fitness.values}")


main()
