import numpy as np
import math
from deap import base, creator, tools
import random
import matplotlib.pyplot as plt
import time
from scipy.optimize import minimize
import json
import pandas as pd


class AlgEvolution:
    def __init__(self, setup):
        self.setup = setup
        self.stats = tools.Statistics(key=lambda ind: ind.fitness.values)
        self.stats.register("avg", np.mean)
        self.stats.register("std", np.std)
        self.stats.register("min", np.min)
        self.stats.register("max", np.max)
        self.logbook = tools.Logbook()
        self.hof = tools.HallOfFame(1)
        self.pop = self.setup.toolbox.population(n=self.setup.POP_SIZE)
        self.hof.update(self.pop)

        self.best_solutions_array = []
        self.best_individual_array = []
        self.fitness_array = []
        self.data = {}
        self.repopulation_counter = 0
        self.allFitnessValues = {}

    def repopulate_best_individuals(self):
        best_individuals = self.hof[: self.setup.POP_SIZE]
        self.pop[:] = best_individuals
        self.repopulation_counter = 0

    def get_population_dataframes(self):
        best_df = pd.DataFrame(self.best_individual_array)
        fitness_df = pd.DataFrame(self.fitness_array)
        return best_df, fitness_df

    def getters(self):
        return {
            "best_fitness_array": self.best_solutions_array,
            "best_individual_array": self.best_individual_array,
        }

    def diversity(self, first_front, first, last):
        """Given a Pareto front `first_front` and the two extreme points of the
        optimal Pareto front, this function returns a metric of the diversity
        of the front as explained in the original NSGA-II article by K. Deb.
        The smaller the value is, the better the front is.
        """
        if len(first_front[0].fitness.values) < 2:
            return float(
                "inf"
            )  # Retorna infinito se não houver valores de aptidão suficientes

        df = math.hypot(
            first_front[0].fitness.values[0] - first[0],
            first_front[0].fitness.values[1] - first[1],
        )
        dl = math.hypot(
            first_front[-1].fitness.values[0] - last[0],
            first_front[-1].fitness.values[1] - last[1],
        )
        dt = [
            math.hypot(
                first.fitness.values[0] - second.fitness.values[0],
                first.fitness.values[1] - second.fitness.values[1],
            )
            for first, second in zip(first_front[:-1], first_front[1:])
        ]

        if len(first_front) == 1:
            return df + dl

        dm = sum(dt) / len(dt)
        di = sum(abs(d_i - dm) for d_i in dt)
        delta = (df + dl + di) / (df + dl + len(dt) * dm)
        return delta

    def apply_elitism(self, population):
        population.sort(key=lambda x: x.fitness.values)
        for i in range(len(self.hof)):
            population[-(i + 1)] = self.setup.toolbox.clone(self.hof[i])

    def repopulate_best_individuals(self):
        if self.repopulation_counter == 25:
            best_individuals = self.hof[: self.setup.POP_SIZE]
            self.pop[:] = best_individuals
            self.repopulation_counter = 0

    def run(self):
        fitnesses = map(self.setup.toolbox.evaluate, self.pop)
        for ind, fit in zip(self.pop, fitnesses):
            ind.fitness.values = [fit]

        for g in range(self.setup.NGEN):

            # print(f"---------------------- Generation {g+1} ---------------------------------------------")

            offspring = self.setup.toolbox.select(self.pop, k=len(self.pop))
            offspring = [self.setup.toolbox.clone(ind) for ind in offspring]

            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < self.setup.CXPB:
                    self.setup.toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:
                if random.random() < self.setup.MUTPB:
                    self.setup.toolbox.mutate(mutant)
                    del mutant.fitness.values

            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(self.setup.toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = [fit]

            self.best_solutions_array.append(self.hof[0].fitness.values)
            # Calcula a média de fitness para cada geração
            avg_fitness_per_generation = np.mean(
                [ind.fitness.values[0] for ind in self.pop]
            )
            desvio_padrao = np.std([ind.fitness.values[0] for ind in self.pop])

            # print(f"Média de fitness na geração {g+1}: {avg_fitness_per_generation}")
            self.data = {}
            self.data["Generations"] = g + 1
            self.data["Variaveis de Decisão"] = self.hof[0]
            self.data["Evaluations"] = self.setup.evaluations
            self.data["Best Fitness"] = self.hof[0].fitness.values
            self.data["Media"] = avg_fitness_per_generation
            self.data["Desvio Padrao"] = desvio_padrao
            self.best_individual_array.append(self.data)

            for ind in self.pop:
                self.allFitnessValues = {}
                self.allFitnessValues["Generations"] = g + 1
                self.allFitnessValues["Fitness"] = ind.fitness.values[0]
                self.allFitnessValues["Evaluations"] = self.setup.evaluations
                self.fitness_array.append(self.allFitnessValues)

            self.hof.update(self.pop)
            self.pop[0] = self.setup.toolbox.clone(self.hof[0])

            # self.apply_elitism(self.pop)
            if (
                self.setup.num_repopulation != 0
                and (g + 1) % self.setup.num_repopulation == 0
            ):
                print("\nRCE being applied!")
                self.repopulate_best_individuals()
                # self.setup.toolbox.repopulate()

            else:
                self.pop[:] = offspring

            record = self.stats.compile(self.pop)
            self.logbook.record(gen=g, **record)
            self.repopulation_counter += 1

        best_df = pd.DataFrame(self.best_individual_array)
        display(best_df)
        # fitness_df = pd.DataFrame(self.fitness_array)
        # display(fitness_df.loc[fitness_df["Generations"] == 4])

        return self.pop, self.logbook, self.hof[0]


class DataExploration:
    def __init__(self):
        self.fit_array = []

    def calculate_stats(self, logbook):

        fit_avg = logbook.select("avg")
        fit_std = logbook.select("std")
        fit_min = logbook.select("min")
        fit_max = logbook.select("max")

        self.fit_array.append(fit_min)
        self.fit_array.append(fit_avg)
        self.fit_array.append(fit_max)
        self.fit_array.append(fit_std)

        return {
            "min_fitness": fit_min,
            "max_fitness": fit_max,
            "avg_fitness": fit_avg,
            "std_fitness": fit_std,
        }

    def visualize(self, logbook, pop, repopulation=False):
        generation = logbook.select("gen")
        statics = self.calculate_stats(logbook)

        if repopulation:
            best_solution_index = statics["min_fitness"].index(
                min(statics["min_fitness"])
            )
            best_solution_variables = pop[best_solution_index]
            best_solution_fitness = statics["min_fitness"][best_solution_index]
        else:
            best_solution_index = statics["min_fitness"].index(
                min(statics["min_fitness"])
            )
            best_solution_variables = logbook.select("min")
            best_solution_fitness = min(statics["min_fitness"])

        print("\nBest solution variables =\n", best_solution_variables)
        print("\nBest solution fitness = ", best_solution_fitness)

        self.grafico_convergencia(generation, statics, repopulation)

        self.plot_population(pop, repopulation)

    def grafico_convergencia(self, gen, lista, repopulation=False):
        fig, ax1 = plt.subplots()
        if repopulation:
            ax1.set_title("Com Repopulação")
        else:
            ax1.set_title("Sem Repopulação")

        if repopulation:
            line1 = ax1.plot(gen, lista["min_fitness"], "*b-", label="Minimum Fitness")
        else:
            line1 = ax1.plot(gen, lista["min_fitness"], "*b-", label="Minimum Fitness")

        line2 = ax1.plot(gen, lista["avg_fitness"], "+r-", label="Average Fitness")
        line3 = ax1.plot(gen, lista["max_fitness"], "og-", label="Maximum Fitness")
        ax1.set_xlabel("Generation")
        ax1.set_ylabel("Fitness")
        lns = line1 + line2 + line3
        labs = [l.get_label() for l in lns]
        ax1.legend(lns, labs, loc="upper right")

    def graficoBarrasFitnessGeneration(self, generation, lista, repopulation=False):
        fig, ax = plt.subplots()
        if repopulation:
            ax.set_title("Com Repopulação")
        else:
            ax.set_title("Sem Repopulação")

        if len(generation) > 1:
            best_solutions = [min(lista["min_fitness"]) for i in range(len(generation))]
            print(best_solutions)
            avg_fitness = lista["avg_fitness"]
            generations = np.arange(2, len(generation) + 1)

            ax.bar(generations, best_solutions, color="b", label="Melhor Fitness")
            ax.plot(
                generations,
                avg_fitness[1:],
                color="r",
                linestyle="--",
                label="Média Fitness por Geração",
            )

            ax.set_xlabel("Geração")
            ax.set_ylabel("Fitness")
            ax.set_title("Melhor Fitness e Média por Geração")
            ax.legend()
            plt.show()

    def plot_best_fitness_generation(self, best_solutions_array, repopulation=False):
        generations = range(2, len(best_solutions_array) + 1)

        # Filtrar listas vazias
        best_fitness = [min(solution) for solution in best_solutions_array if solution]
        avg_fitness = [
            np.mean(solution) for solution in best_solutions_array if solution
        ]

        print(len(best_fitness), len(avg_fitness))

        plt.figure()
        plt.bar(generations, best_fitness, color="b", label="Melhor Fitness")
        plt.plot(
            generations,
            avg_fitness,
            color="r",
            linestyle="--",
            label="Média Fitness por Geração",
        )

        plt.xlabel("Geração")
        plt.ylabel("Fitness")
        plt.title("Melhor Fitness e Média por Geração")
        plt.legend()
        plt.grid(True)
        if repopulation:
            plt.title("Com Repopulação")
        else:
            plt.title("Sem Repopulação")
        plt.show()

    def plot_population(self, population, repopulation=False):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        if repopulation:
            ax.set_title("Com Repopulação")
        else:
            ax.set_title("Sem Repopulação")

        x_values = [ind[0] for ind in population]
        y_values = [ind[1] for ind in population]
        z_values = [ind[2] for ind in population]

        ax.scatter(x_values, y_values, z_values, c="b", label="Population")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend()
        ax.grid(True)

        plt.show()


class Setup:
    def __init__(self, params):
        self.params = params
        self.CXPB = params["CXPB"]
        self.MUTPB = params["MUTPB"]
        self.NGEN = params["NGEN"]
        self.POP_SIZE = params["POP_SIZE"]
        self.IND_SIZE = params["IND_SIZE"]
        self.CROSSOVER, self.MUTACAO, self.NUM_GENES, self.POPULATION_SIZE = (
            0.9,
            0.05,
            100,
            100,
        )
        self.SIZE_INDIVIDUAL = 10
        self.evaluations = 0
        self.num_repopulation = int(self.NUM_GENES * 0.20)
        self.dataset = {}
        self.beta_constants = {}

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        self.toolbox = base.Toolbox()
        self.toolbox.register("attribute", random.random)
        self.toolbox.register(
            "individual",
            tools.initRepeat,
            creator.Individual,
            self.toolbox.attribute,
            n=self.SIZE_INDIVIDUAL,
        )
        self.toolbox.register(
            "population", tools.initRepeat, list, self.toolbox.individual
        )

        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=3)
        self.toolbox.register("evaluate", self.evaluate)
        # self.toolbox.register("repopulate", self.repopulate_best_individuals)

    def gerarDataset(self, excel):
        df = pd.read_excel(excel)
        print(df.columns)
        self.dataset = {
            "CXPB": self.CROSSOVER,
            "TAXA_MUTACAO": self.MUTACAO,
            "NUM_GEN": self.NUM_GENES,
            "POP_SIZE": self.POPULATION_SIZE,
            "IND_SIZE": self.SIZE_INDIVIDUAL,
            "evaluations": self.evaluations,
            "NUM_REPOPULATION": self.num_repopulation,
        }

    def evaluate(self, individual):
        self.evaluations += 1
        rastrigin = 10 * self.SIZE_INDIVIDUAL
        for i in range(self.SIZE_INDIVIDUAL):
            rastrigin += individual[i] * individual[i] - 10 * (
                math.cos(2 * np.pi * individual[i])
            )
        return rastrigin

    def rosenbrock(self, x):
        return np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)

    def globalSolutions(self):
        n_dimensions = 2

        try:
            rastrigin_result = minimize(
                self.evaluate, x0=np.zeros(n_dimensions), method="BFGS"
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


def main():

    tempo1 = time.time()

    # Setup
    params = load_params(
        "/home/pedrov/Documentos/GitHub/Engenharia-Eletrica-UFF/Iniciação Cientifica - Eng Eletrica UFF/evolution_rce_master/src/db/parameters.json"
    )
    print(params)
    data_visual = DataExploration()
    setup = Setup(params)
    alg = AlgEvolution(setup)

    # Com repopulação loop
    print("\nAlg evolutivo com repopulação")
    pop_with_repopulation, logbook_with_repopulation, best_with_repopulation = alg.run()

    # Visualização dos resultados
    data_visual.visualize(
        logbook_with_repopulation, pop_with_repopulation, repopulation=True
    )

    tempo2 = time.time()
    print(f"Total execution time: {round(tempo2-tempo1,2)} seconds")


main()
