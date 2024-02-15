from individuals import Individual
from population import Population
from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm(population_size=100)
    ga.run(generations=50)


if __name__ == "__main__":
    main()
