# lambda functions
'''
instead of doing a function like this, we can do a lambda functions, that is looking more elegant.

def full_name_oldest_way(name, lastname):
    return f'My full name is {name.title()} {lastname.title()}'

'''

full_name = lambda name, lastname: f'My full name is {name.title()} {lastname.title()}'
result = full_name('jorge', 'garcia')
print(result)

multiplication = lambda x, y: x * y
result = multiplication(10, 20)
print(result)

# lambda function with if else statement
even_or_odd = lambda x: f'{x} is even' if x % 2 == 0 else f'{x} is odd'
print(even_or_odd(33))
print(even_or_odd(20))

greater_smaller_equal = lambda x, y: f'{x} is smaller than {y}' if x < y else \
    f'{x} is greater than {y}' if x > y else f'{x} and {y} are equal'
print(greater_smaller_equal(20, 21))
print(greater_smaller_equal(25, 20))
print(greater_smaller_equal(20, 20))


# high order functions with lambdas 
sum = lambda x, y: x + y

'''
In this function we recive a number and a function as a parameters to then make a sum with the number and 
the result of the function passed as a parameter
'''
perform_sum = lambda x, func: x + func(x, x +20)
result = perform_sum(20, sum)

print(result)


