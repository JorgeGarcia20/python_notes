import random
import sys

'''
1. debo generar la respuesta del computador
2. debo hacer una funcion que pida la respuesta al usuario
3. debo hacer una funcion que cheque las reglas
4. debo crear una funcion que ejecute el juego y lleve un conteo de las rondas.
    dentro de esta funcion debo de comparar la cantidad de ronda que ha ganado el computador o el usuario
    si las rondas ganadas son dos entonces debo de detener el juego y imprimir un mensaje de quien ha ganado.
'''


options = ('piedra', 'papel', 'tijera')


def get_computer_move():
    return random.choice(options)


def get_user_move():
    user_move = input('piedra, papel o tijeras => ')
    return user_move.lower()


def is_correct_move(user_move):
    return user_move in options


def check_rules(user_move, computer_move, user_wins, computer_wins):
    
    PIEDRA_TIJERA = 'Piedra gana a Tijera'
    PAPEL_PIEDRA = 'Papel gana a Piedra'
    TIJERA_PAPEL = 'Tijera gana a Papel'
    
    USER_WIN = 'El usuario gana esta ronda!'
    COMPUTER_WIN = 'El computador gana esta ronda!'

    if user_move == computer_move:
        print('Empate!')

    elif user_move == 'piedra':
        if computer_move == 'tijera':
            print(PIEDRA_TIJERA)
            print(USER_WIN)
            user_wins += 1
        else:
            print(PAPEL_PIEDRA)
            print(COMPUTER_WIN)
            computer_wins += 1
    elif user_move == 'papel':
        if computer_move == 'piedra':
            print(PAPEL_PIEDRA)
            print(USER_WIN)
            user_wins += 1
        else:
            print(PIEDRA_TIJERA)
            print(COMPUTER_WIN)
            computer_wins += 1
    elif user_move == 'tijera':
        if computer_move == 'papel':
            print(TIJERA_PAPEL)
            print(USER_WIN)
            user_wins += 1
        else:
            print(PIEDRA_TIJERA)
            print(COMPUTER_WIN)
            computer_wins += 1
    return user_wins, computer_wins

def check_winer(user_wins, computer_wins):
    if user_wins == 2:
        sys.exit('El usuario gana el juego!')
    elif computer_wins == 2:
        sys.exit('El computador gana el juego!')


def run_game():
    
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        computer_move = get_computer_move()
        user_move = get_user_move()

        rounds += 1

        if not is_correct_move(user_move):
            print('esa opcion no es valida')
            continue

        print('User option =>', user_move)
        print('Computer option =>', computer_move)

        user_wins, computer_wins = check_rules(user_move, computer_move, user_wins, computer_wins)

        check_winer(user_wins, computer_wins)            

run_game()


