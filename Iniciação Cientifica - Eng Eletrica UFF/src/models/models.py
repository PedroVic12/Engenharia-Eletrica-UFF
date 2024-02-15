from collections import Counter
from faker import Faker
import random
import numpy as np

fake = Faker("pt_BR")


class Individual:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f"Individual(Name: {self.name}, Age: {self.age}, Sex: {self.sex})"


class Population:
    def __init__(self, size):
        self.individuals = []
        self.size = size
        self._generate_initial_population()

    def _generate_initial_population(self):
        for _ in range(self.size):
            name = fake.name()
            age = fake.random_int(18, 80)
            sex = random.choice(["M", "F"])
            self.individuals.append(Individual(name, age, sex))

    def select_individuals(self, sex, age):
        return [ind for ind in self.individuals if ind.sex == sex and ind.age == age]
