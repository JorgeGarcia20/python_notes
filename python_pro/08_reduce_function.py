import functools
import random


numbers = [n for n in range(1, random.randint(1, 21))]


def sum_numbers(counter, item):
    print(f'Counter => {counter}')
    print(f'Item => {item}')
    return counter + item


# sum_items = functools.reduce(lambda counter, item: counter + item, numbers)
sum_items = functools.reduce(sum_numbers, numbers)
print(sum_items)