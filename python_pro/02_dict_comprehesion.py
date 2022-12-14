from random import randint
# DICTIONARY COMPREHENSION

countries = ['Mexico', 'Venezuela', 'Argentina', 'Colombia', 'Guatemala']
population = {country: randint(100, 1000) for country in countries}
print(population)


population_v2 = {c: p for c, p in population.items() if p < 400}
print(population_v2)


greeting = 'Hello, i am Jorge, nice to meet you'
vowels_text = {v: v.upper() for v in greeting if v in ['a', 'e', 'i', 'o', 'u']}
print(vowels_text)


# challenge
count_vowels_text = {v: greeting.count(v) for v in greeting if v in ['a', 'e', 'i', 'o', 'u']}
print(count_vowels_text)


names = ['Jorge', 'Alberto', 'Carlos', 'Jose', 'Maria', 'Carmen']
ages = [23, 22, 21, 30, 29, 28]

# match an item from the names list with an item from the ages list and returns a list of tuples with the matched items
users = list(zip(names, ages))
# print(users)

users = {name: age for (name, age) in zip(names, ages)}
print(users)

