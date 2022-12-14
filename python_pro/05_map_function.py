import random

numbers = [n for n in range(1, random.randint(1, 51))]

evens = lambda x: f'{x} is even' if x % 2 == 0 else x

result = list(map(evens, numbers))
print(result)


fizz_buzz_lambda = lambda number : 'fizzbuzz' if number % 3 == 0 and number % 5 == 0 \
                                                else 'fizz' if number % 3 == 0 \
                                                else 'buzz' if number % 5  == 0 \
                                                else str(number)

fizz_buzz_list = list(map(fizz_buzz_lambda, numbers))
print(fizz_buzz_list)

# in process
# is_prime = lambda number: f'{number} is prime' if number % 1 == 0 and number % 2 != 0 else number

def is_prime(number):
    if number <= 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
        

prime_list = list(map(is_prime, numbers))
print(prime_list)