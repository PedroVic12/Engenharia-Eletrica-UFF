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
        self.CONJUNTO_ELITE_RCE = set()

    #!RCE
    def apply_RCE(self, population):
        """Aplicar o critério de repopulação com elitismo (RCE)"""

        # Adicionar o melhor indivíduo da população atual ao conjunto elite
        # self.addBestIndividualOfGenerationToRCE()

        # All individuos gerados
        all_df = pd.DataFrame(self.allIndividualValuesArray)
        print("TAMANHO ATUAL DE TODOS INDIVIDUOS", all_df.shape[0])
        self.add_best_individual_to_RCE(all_df)

        # Critério 1
        best_ind_array = self.select_best_elitismo_RCE(all_df)

        # Critério 2
        self.conjuntoElite(best_ind_array)

        # Critério 3
        self.generateConjuntoEliteWithRandomPopulation()

        # Repopulate
        elite_with_fitness = [
            ind for ind in self.CONJUNTO_ELITE_ARRAY if ind.fitness.values
        ]
        new_population = self.repopulate_RCE(self.pop, elite_with_fitness)
        return new_population

    def elitismoSimples(self):
        # print("\nSimple Elitism being applied! in Generation:", current_generation + 1)
        self.hof.update(self.pop)
        best_individual = None

        # Encontrar o melhor indivíduo do hall da fama com um fitness válido e maior que 0.0
        for ind in self.hof:
            if ind.fitness.valid and ind.fitness.values[0] != 0.0:
                print("Melhor indivíduo encontrado!", ind.fitness.values[0])
                best_individual = ind
                break

        # Verificar se o melhor indivíduo foi encontrado e se seu fitness não é (0, 0)
        if best_individual is not None and best_individual.fitness.values != (0, 0):
            # Atualizar o primeiro indivíduo da população com o melhor indivíduo encontrado
            self.pop[0] = self.setup.toolbox.clone(best_individual)

    def add_best_individual_to_RCE(self, df):
        # Encontrar o índice da linha com o menor fitness
        index_min_fitness = df["Fitness"].idxmin()

        # Obter os valores da linha com o menor fitness
        best_individual_values = df.loc[[index_min_fitness]]
        best_individual_values["RCE"] == "SIM"
        print(
            "\n\nMelhor da geração:",
            str(best_individual_values["Generations"])[5:].strip(),
        )
        display(best_individual_values)
        print(best_individual_values["Fitness"].values[0])
        # Adicionar os valores ao array self.pop_RCE
        if not (
            best_individual_values["Fitness"].values[0] == 0.0
            or len(best_individual_values["Fitness"].values) == 0,
        ):

            self.pop_RCE.append(best_individual_values.to_dict("records")[0])
            print("Melhor da geração Adicionado no RCE!")

    def conjuntoElite(self, best_ind_1, delta=1):
        """Comparar as variáveis de decisão de cada indivíduo e verificar se existem 3 diferentes."""
        isDiferente = False
        self.cout(
            "CRITÉRIO 2 - Comparar as variáveis de decisão de cada indivíduo e verificar se existem 3 diferentes."
        )

        # Loop sobre os indivíduos da geração atual
        for i in range(len(best_ind_1)):
            current_individual = best_ind_1[i]
            # print("\n---> Indivíduo atual:", current_individual["index"])
            # Verificar se o fitness do indivíduo é zero
            if current_individual["Fitness"] == 0.0:
                continue
            # Loop sobre os outros indivíduos
            for j in range(i + 1, len(best_ind_1)):
                other_individual = best_ind_1[j]

                if current_individual["Generations"] == other_individual["Generations"]:
                    # print(                        f"---> Geração atual {current_individual['Generations'] + 1} - {current_individual['index']}x{other_individual['index']}"                    )

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
                        # print("\ncalculando...")
                        # print(f"{current_var}x{other_var}")

                        # Verificar se a diferença entre as variáveis de decisão é maior do que o delta
                        if abs(current_var - other_var) > delta:
                            diff_counter += 1

                    # Se o número de diferenças for maior ou igual a 3 e o indivíduo ainda não tiver sido adicionado, adicionamos ao conjunto elite
                    if (
                        diff_counter >= 3
                        and current_individual["index"] not in self.CONJUNTO_ELITE_RCE
                    ):
                        isDiferente = True
                        self.pop_RCE.append(current_individual)
                        self.CONJUNTO_ELITE_RCE.add(
                            current_individual["index"],
                            # current_individual["Variaveis de Decisão"],
                        )
                        print(
                            f"Indivíduo Index({current_individual['index']}) diferente adicionado ao conjunto elite:  O.O  "
                        )

        # Se encontrarmos pelo menos um indivíduo com as condições especificadas, exibimos o conjunto elite
        if isDiferente:
            print("Conjunto Elite atualizado!  ultimo inserido = ", self.pop_RCE[-1])

        else:
            print("Nenhum indivíduo atende aos critérios.")

    def addBestIndividualOfGenerationToRCE(self):
        # Adicionar o melhor indivíduo da população atual ao conjunto elite
        best_current_ind = self.pop[
            self.pop.index(self.hof[0])
        ]  # Melhor indivíduo da população atual
        print("Best Current Individuo", best_current_ind.fitness.values[0], "\n")
        if best_current_ind not in self.pop_RCE:
            self.pop_RCE.append(best_current_ind)

    def select_best_elitismo_RCE(self, df, k=0.3):
        """Seleciona 30% dos melhores indivíduos de cada geração."""
        self.cout(f"CRITÉRIO 1 RCE - 30% dos melhores fitness de cada geração")

        # Fatiando o dataframe para obter os 30% melhores indivíduos de cada geração
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
            _df = pd.DataFrame(best_individuals)
            new_df_sorted = _df[_df["Generations"] == i].sort_values(
                by=["Fitness"], ascending=False
            )
            if new_df_sorted.shape[0] > 0:
                # print(                    f"Total de individuos selecionados da geração {i} ={new_df_sorted.shape[0]} ",                )
                continue
                # display(new_df_sorted[:taxa])
            else:
                # print("Nenhum individuo selecionado na geração atual")
                continue

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
        self.cout("CRITERIO 3 - CONJUNTO ELITE (20%) com o restante aleatorio(80%)")
        try:
            RCE_df = pd.DataFrame(self.pop_RCE)

            # pegando as porcentagem
            elite = len(self.pop_RCE) * 0.2
            elite = int(math.ceil(elite))
            random_population = len(self.pop) * 0.8
            print(
                f"Taxa Candidatos elite (20% de {len(self.pop_RCE)}) = {elite} | random (80% de {len(self.pop)})= {random_population}"
            )
            # print("\n\nCandidatos Conjunto Elite")
            # TODO display(RCE_df[:elite])
            # self.combinar_aleatoriamente()

        except Exception as e:
            print("Erro ao gerar novo conjunto elite", e)

    #! Main LOOP
    def run(self, RCE=False, decision_variables=None, fitness_function=None):
        # Avaliar o fitness da população inicial
        fitnesses = map(self.setup.toolbox.evaluate, self.pop)
        for ind, fit in zip(self.pop, fitnesses):
            ind.fitness.values = [fit]

        if decision_variables is None and fitness_function is None:
            # Gerar variáveis de decisão aleatórias para os indivíduos
            decision_variables = [
                random.random() for _ in range(self.setup.SIZE_INDIVIDUAL)
            ]

            # Definir a função de fitness padrão como a função Rastrigin
            fitness_function = self.setup.rastrigin_decisionVariables

        # Restante do código permanece o mesmo
        # Verificar se as variáveis de decisão e a função de fitness foram fornecidas
        if decision_variables is None or fitness_function is None:
            # Verificar se as variáveis de decisão e a função de fitness foram definidas
            if not hasattr(self, "decision_variables") or not hasattr(
                self, "fitness_function"
            ):
                raise ValueError(
                    "Variáveis de decisão e função de fitness não definidas. Use set_decision_variables_and_fitness_function primeiro."
                )
        else:
            self.decision_variables = decision_variables
            self.fitness_function = fitness_function

            # Definir a função de fitness com base na função fornecida
            def fitness_func(individual):
                return self.fitness_function(individual, self.decision_variables)

            # Registrar a função de fitness no toolbox
            self.setup.toolbox.register("evaluate", fitness_func)

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

            # Avaliar o fitness dos novos indivíduos |
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

            if (
                self.data["Best Fitness"] == -0.0
                or self.data["Best Fitness"] == set()
                or self.data["Best Fitness"] == 0.0
            ):

                continue
            else:
                self.best_individual_array.append(self.data)

            self.visualizarPopAtual(
                current_generation, [avg_fitness_per_generation, std_deviation]
            )

            # Aplicar repopulação e elitismo
            self.elitismoSimples()

            if RCE and (
                self.setup.num_repopulation != 0
                and (current_generation + 1) % self.setup.num_repopulation == 0
            ):

                print(
                    f"\nRCE being applied!  - Generation = {current_generation + 1} ",
                )
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
            datasetIndividuals = {
                "Generations": geracaoAtual + 1,
                "index": i,
                "Variaveis de Decisão": self.pop[i],
                "Fitness": self.pop[i].fitness.values[0],
                "Media": stats[0],
                "Desvio Padrao": stats[1],
                "RCE": " - ",
            }
            self.allIndividualValuesArray.append(datasetIndividuals)

    def cout(self, msg):
        print(
            "\n=========================================================================================================="
        )
        print("\t", msg)
        print(
            "==========================================================================================================\n"
        )

    def combinar_aleatoriamente(self):
        try:
            elite_size = len(self.pop_RCE)
            elite_df = pd.DataFrame(self.pop_RCE)

            # Filtrar os indivíduos restantes da última geração
            all_df = pd.DataFrame(self.allIndividualValuesArray)
            remaining_individuals = all_df[
                all_df["Generations"] == all_df["Generations"].max()
            ]

            # Remover os indivíduos do conjunto elite da lista dos restantes
            remaining_individuals = remaining_individuals[
                ~remaining_individuals.index.isin(elite_df.index)
            ]

            # Selecionar aleatoriamente os indivíduos restantes da última geração para preencher
            random_individuals = remaining_individuals.sample(n=100 - elite_size)

            # Adicionar a coluna "RCE" e definir como "SIM" para os indivíduos do conjunto elite e "NÃO" para os outros
            elite_df["RCE"] = "SIM"
            random_individuals["RCE"] = "NÃO"

            # Combinar os indivíduos do conjunto elite com os indivíduos aleatórios
            new_df = pd.concat([elite_df, random_individuals])
            display(new_df)
            return new_df
        except Exception as e:
            print("Erro ao combinar aleatoriamente", e)
