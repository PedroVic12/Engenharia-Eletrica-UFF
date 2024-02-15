from collections import Counter
from faker import Faker
import random

# Create a Faker object for Brazilian Portuguese
fake = Faker("pt_BR")


class Model:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __repr__(self):
        return f"Model(nome={self.nome}, idade={self.idade}, sexo={self.sexo})"


def gerar_dados(quantidade):
    """Generate random person data."""
    return [
        Model(fake.name(), fake.random_int(min=18, max=80), random.choice(["M", "F"]))
        for _ in range(quantidade)
    ]


def filtrar(sexo, idade):
    """Filter the population by  gender and age."""
    return [
        pessoa for pessoa in population if pessoa.sexo == sexo and pessoa.idade <= idade
    ]


# Generate a population of individuals
population = gerar_dados(1000)
for i in range(1, len(population)):
    # print(f"{i} - {population[i]}")
    pass

# Count the number of individuals by sex and age
contador = Counter((pessoa.sexo, pessoa.idade) for pessoa in population)

# Select the top 30% of individuals who are male and 25 years old
selecionados = filtrar("M", 25)
print(f"População filtrada = {selecionados}")


# Now we want to calculate the top 30%
top_30_percent = int(0.3 * len(selecionados))

# Sort by health or any other criteria and select the top 30%
selecionados_sorted = sorted(selecionados, key=lambda x: x.idade, reverse=True)
selecionados_top_30 = selecionados_sorted[:top_30_percent]

print(f"Top 30% selected individuals: {selecionados_top_30}")
