# LIST COMPREHENSION

# Coolest way to fill a list
numbers = [number for number in range(1, 21)]
print(numbers)


# List comprehension with if statement
numbers = [number * 2 for number in range(1, 41) if number % 2 == 0]
print(numbers)


# List comprehension with if else statement
numbers = [number if number % 2 == 0 else 0 for number in range(1, 31)]
print(numbers)


def fizz_buzz(number):
    is_multiple_of_three = number % 3 == 0
    is_multiple_of_five = number % 5 == 0

    if is_multiple_of_three and is_multiple_of_five:
        return 'FizzBuzz'
    elif is_multiple_of_three:
        return 'Fizz'
    elif is_multiple_of_five:
        return 'Buzz'
    else:
        return str(number)


fizz_buzz_list = [fizz_buzz(number) for number in range(1, 101)]
print(fizz_buzz_list)
