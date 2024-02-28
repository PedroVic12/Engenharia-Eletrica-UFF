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
        self.pop_RCE = []
        self.hof.update(self.pop)

        self.best_solutions_array = []
        self.best_individual_array = []
        self.fitness_array = []
        self.CONJUNTO_ELITE_ARRAY = []
        self.allIndividualValuesArray = []
        self.data = {}
        self.repopulation_counter = 0
        self.allFitnessValues = {}
        self.validateCounter = 0

    #!RCE
    def elitismoSimples(self, current_generation):
        print("\nSimple Elitism being applied! in Generation:", current_generation + 1)
        self.hof.update(self.pop)
        self.pop[0] = self.setup.toolbox.clone(self.hof[0])

    def conjuntoElite(self, best_ind_1, delta=1):
        """Comparar as variáveis de decisão de cada indivíduo e verificar se existem 3 diferentes."""
        isDiferente = False
        already_added = (
            set()
        )  # Conjunto para armazenar as variáveis de decisão dos indivíduos já adicionados

        # Loop sobre os indivíduos da geração atual
        for i in range(len(best_ind_1)):
            current_individual = best_ind_1[i]
            print("\n---> Indivíduo atual:", current_individual["index"])

            # Loop sobre os outros indivíduos para comparar
            for j in range(i + 1, len(best_ind_1)):
                other_individual = best_ind_1[j]

                if current_individual["Generations"] == other_individual["Generations"]:
                    print(
                        f"---> Geração atual {current_individual['Generations']} - {current_individual['index']}x{other_individual['index']}"
                    )

                    # Contador para acompanhar o número de diferenças entre as variáveis de decisão
                    diff_counter = 0

                    # Loop sobre as variáveis de decisão para comparar
                    for var_index in range(
                        len(current_individual["Variaveis de Decisão"])
                    ):
                        current_var = current_individual["Variaveis de Decisão"][
                            var_index
                        ]
                        other_var = other_individual["Variaveis de Decisão"][var_index]
                        print(f"{current_var}x{other_var}")

                        # Verificar se a diferença entre as variáveis de decisão é maior do que o delta
                        if abs(current_var - other_var) > delta:
                            diff_counter += 1

                    # Se o número de diferenças for maior ou igual a 3 e o indivíduo ainda não tiver sido adicionado, adicionamos ao conjunto elite
                    if (
                        diff_counter >= 3
                        and current_individual["index"] not in already_added
                    ):
                        isDiferente = True
                        self.pop_RCE.append(current_individual)
                        already_added.add(
                            current_individual["index"]
                        )  # Adiciona as variáveis de decisão ao conjunto already_added
                        print(
                            "Indivíduo adicionado ao conjunto elite:",
                            current_individual["index"],
                        )

        # Se encontrarmos pelo menos um indivíduo com as condições especificadas, exibimos o conjunto elite
        if isDiferente:
            print("Conjunto Elite atualizado!  ultimo inserido = ", self.pop_RCE[-1])

        else:
            print("Nenhum indivíduo atende aos critérios.")

        

    def determinate_ConjuntoElite(self, best_ind_1, delta=3):
        """Comparar as 5 variaveis de decisao de de cada inviduo e verfiicar se tem 3 diferentes."""
        isDiferente = False

        # checar valores iguais
        # print(self.pop[0])
        for i in range(0, len(best_ind_1)):
            if best_ind_1[i]["Generations"] == best_ind_1[i + 1]["Generations"]:
                print("\n---> Geração atual", best_ind_1[i]["Generations"])
                print(
                    "\n\nComparando",
                    best_ind_1[i]["Generations"],
                    best_ind_1[i]["index"],
                    best_ind_1[i]["Variaveis de Decisão"][0],
                )
                print(
                    best_ind_1[i + 1]["Generations"],
                    best_ind_1[i + 1]["index"],
                    best_ind_1[i + 1]["Variaveis de Decisão"][0],
                )

                if (
                    best_ind_1[i]["Variaveis de Decisão"][0]
                    >= best_ind_1[i + 1]["Variaveis de Decisão"][0]
                ):
                    print("Variavel 1 igual ou maior")
                    self.validateCounter += 1
                    if self.validateCounter > delta:
                        isDiferente = True
                        self.pop_RCE.append(best_ind_1[i])
            else:
                break

        # Critério diferença minima das variaveis de decisao entre 3 melhores solucoes
        if isDiferente:
            self.pop_RCE.append(self.pop[0])
            print(self.pop_RCE)
        else:
            print(len(self.pop))
            print("Esse individuo tem que ser selecionado novamente")

    def apply_RCE(self, population):
        df = pd.DataFrame(self.allIndividualValuesArray)
        best_ind = self.select_best_elitismo_RCE(df)
        self.conjuntoElite(best_ind)
        self.compareIndividual()

        #!Repopulate
        # Filtrar os indivíduos com fitness não nulo
        elite_with_fitness = [
            ind for ind in self.CONJUNTO_ELITE_ARRAY if ind.fitness.values
        ]
        new_population = self.repopulate_RCE(self.pop, elite_with_fitness)

    def select_best_elitismo_RCE(self, df, k=0.3):
        taxa = int(self.setup.POP_SIZE * k)
        best_individuals = []
        for i in range(1, self.setup.NGEN):

            # Ordenar os dados pela coluna "Fitness" em ordem decrescente
            df_sorted = df[df["Generations"] == i].sort_values(
                by=["Fitness"], ascending=False
            )

            top_10 = df_sorted[:taxa]

            # Converter os top 10 indivíduos para um dicionário e adicionar à lista
            top_10_dict = top_10.to_dict("records")
            best_individuals.extend(top_10_dict)

        # Retornar a lista de top 10 indivíduos de todas as gerações
        return best_individuals

    def repopulate_RCE(self, population, elite):
        """Realiza a repopulação substituindo parte da população pelo conjunto elite."""
        new_population = elite[:]
        remaining = len(population) - len(elite)
        new_population.extend(random.choices(population, k=remaining))
        # Avaliar o fitness dos novos indivíduos
        fitnesses = map(self.setup.toolbox.evaluate, new_population)
        for ind, fit in zip(new_population, fitnesses):
            ind.fitness.values = [fit]

        # Atualizar o hall da fama com os melhores indivíduos da nova população
        self.hof.update(new_population)

    def compareIndividual(self, delta=3):
        """Comparar as 5 variaveis de decisao de de cada inviduo e verfiicar se tem 3 diferentes."""

        # checar valores iguais

        # comparar individuos
        for i in range(0, len(self.CONJUNTO_ELITE_ARRAY)):
            for j in range(i + 1, len(self.CONJUNTO_ELITE_ARRAY)):
                result = self.pop[i] > self.pop[i]
                if result <= delta:
                    self.CONJUNTO_ELITE_ARRAY.append(self.pop[i]["variables"][i][j])

    def generateConjuntoEliteWithRandomPopulation(
        self,
    ):
        # Critério Pegar os melhores o CONJUNTO ELITE (20%) com o restante aleatorio(80%)
        pass

    #! Main LOOP
    def run(self, RCE=False):
        # Avaliar o fitness da população inicial
        fitnesses = map(self.setup.toolbox.evaluate, self.pop)
        for ind, fit in zip(self.pop, fitnesses):
            ind.fitness.values = [fit]

        # Loop principal através das gerações
        for current_generation in range(self.setup.NGEN):

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

            # Avaliar o fitness dos novos indivíduos | todo RCE here
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(self.setup.toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = [fit]

            # Registrar estatísticas e melhores soluções
            avg_fitness_per_generation = np.mean(
                [ind.fitness.values[0] for ind in self.pop]
            )
            std_deviation = np.std([ind.fitness.values[0] for ind in self.pop])

            #! PEgandos os dados e colocando no df
            self.data = {
                "Generations": current_generation + 1,
                "Variaveis de Decisão": self.hof[0],
                "Evaluations": self.setup.evaluations,
                "Best Fitness": self.hof[0].fitness.values,
                "Media": avg_fitness_per_generation,
                "Desvio Padrao": std_deviation,
            }
            self.best_individual_array.append(self.data)

            self.visualizarPopAtual(
                current_generation, [avg_fitness_per_generation, std_deviation]
            )

            # Aplicar repopulação e elitismo
            self.elitismoSimples(current_generation)

            if RCE and (
                self.setup.num_repopulation != 0
                and (current_generation + 1) % self.setup.num_repopulation == 0
            ):

                print("\nRCE being applied!")
                self.apply_RCE(offspring)
                # self.plot_conjuntoElite()

            else:
                self.pop[:] = offspring

            # Registrar estatísticas no logbook
            record = self.stats.compile(self.pop)
            self.logbook.record(gen=current_generation, **record)

        # Retornar população final, logbook e elite
        return self.pop, self.logbook, self.hof[0]

    def visualizarPopAtual(self, geracaoAtual, stats):
        for i in range(len(self.pop)):
            # print(i, self.pop[i], self.pop[i].fitness.values)
            datasetIndividuals = {
                "Generations": geracaoAtual + 1,
                "index": i,
                "Variaveis de Decisão": self.pop[i],
                "Fitness": self.pop[i].fitness.values,
                "Media": stats[0],
                "Desvio Padrao": stats[1],
            }
            self.allIndividualValuesArray.append(datasetIndividuals)
