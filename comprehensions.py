import random

countries = ['col', 'pe', 'bol', 've']

population = {country: random.randint(1, 100) for country in countries}

print(population)

big_population = {country: population for (country, population) in population.items() if population > 50}
print(big_population)