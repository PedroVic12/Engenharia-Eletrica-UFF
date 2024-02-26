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
                # self.repopulate_best_individuals()
                self.setup.toolbox.repopulate()

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
