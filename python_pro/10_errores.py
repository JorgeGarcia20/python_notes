# defining a custom exception
class YoungerError(Exception):
    pass

x = int(input('Enter a number: '))
y = int(input('Enter anoter number: '))

division = lambda x, y : x / y

try:
    division(x, y)
    if y  == 0:
        raise ZeroDivisionError('You cannot divide by zero!')
except ZeroDivisionError as ex:
    print(ex)


age = int(input('Enter your age: '))

try:
    if age < 18:
        raise YoungerError('You are still a minor')
    else:
        print('Welcome!')
except YoungerError as ex:
    print(ex)

print('end of the program')




