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

    def apply_RCE(self):
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
        """Ordena a população com base nos valores de aptidão dos indivíduos, em ordem crescente. os melhores indivíduos da elite são adicionados à população atual, substituindo os piores indivíduos, com base na ordem crescente de aptidão."""
        population.sort(key=lambda x: x.fitness.values)
        for i in range(len(self.hof)):
            population[-(i + 1)] = self.setup.toolbox.clone(self.hof[i])

    def apply_RCE(self):
        self.validate_RCE()

    def validate_RCE(self):
        if self.repopulation_counter == 25:
            return True

        # Critério 30% do elitismo

        # Critério diferença minima das variaveis de decisao entre 3 melhores solucoes

        # Critério Pegar os melhores o CONJUNTO ELITE (20%) com o restante aleatorio(80%)

        else:
            return False

    def run(self, RCE=False):
        # Avaliar o fitness da população inicial
        fitnesses = map(self.setup.toolbox.evaluate, self.pop)
        for ind, fit in zip(self.pop, fitnesses):
            ind.fitness.values = [fit]

        # Loop principal através das gerações
        for g in range(self.setup.NGEN):

            # Selecionar os indivíduos para reprodução
            offspring = self.setup.toolbox.select(self.pop, k=len(self.pop))
            offspring = [self.setup.toolbox.clone(ind) for ind in offspring]

            # Aplicar crossover
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < self.setup.CXPB:
                    self.setup.toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            # Aplicar mutação
            for mutant in offspring:
                if random.random() < self.setup.MUTPB:
                    self.setup.toolbox.mutate(mutant)
                    del mutant.fitness.values

            # Avaliar o fitness dos novos indivíduos
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(self.setup.toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = [fit]

            # Registrar estatísticas e melhores soluções
            avg_fitness_per_generation = np.mean(
                [ind.fitness.values[0] for ind in self.pop]
            )
            std_deviation = np.std([ind.fitness.values[0] for ind in self.pop])

            self.data = {
                "Generations": g + 1,
                "Variaveis de Decisão": self.hof[0],
                "Evaluations": self.setup.evaluations,
                "Best Fitness": self.hof[0].fitness.values,
                "Media": avg_fitness_per_generation,
                "Desvio Padrao": std_deviation,
            }
            self.best_individual_array.append(self.data)

            for ind in self.pop:
                self.allFitnessValues = {
                    "Generations": g + 1,
                    "Fitness": ind.fitness.values[0],
                    "Evaluations": self.setup.evaluations,
                }
                self.fitness_array.append(self.allFitnessValues)

            # Aplicar repopulação ou elitismo
            if (
                self.setup.num_repopulation != 0
                and (g + 1) % self.setup.num_repopulation == 0
            ):
                if RCE:
                    print("\nRCE being applied!")
                    self.apply_RCE()
                    # self.plot_conjuntoElite()

                else:
                    print("\nSimple Elitism being applied! in Generation:", g + 1)

                    # Atualizar a elite e a população
                    self.hof.update(self.pop)
                    self.pop[0] = self.setup.toolbox.clone(self.hof[0])
            else:
                self.pop[:] = offspring

            # Registrar estatísticas no logbook
            record = self.stats.compile(self.pop)
            self.logbook.record(gen=g, **record)
            self.repopulation_counter += 1

        # Criar DataFrame com as melhores soluções
        best_df = pd.DataFrame(self.best_individual_array)
        display(best_df)

        # Retornar população final, logbook e elite
        return self.pop, self.logbook, self.hof[0]
