import random

options = ("piedra", "papel", "tijeras")

win = ("piedratijeras", "tijeraspapel", "papelpiedra")

rounds = 1

user_wins = 0

computer_wins = 0

def game_stats(rounds, user_wins, computer_wins):
    print("*" * 10)

    print("Ronda", rounds, ": ")

    print("*" * 10)

    print("Victorias de user: ", user_wins, "/ 2")

    print("Victorias de computer: ", computer_wins, "/ 2")

    print("*" * 10)

    print("Elige una opcion: ") 

def player_options_selection():
    options = ("piedra", "papel", "tijeras")
    user_option = input('piedra, papel o tijeras => ')
    user_option = user_option.lower()

    while not user_option in options:
        print("Elige una opcion valida: ")
        user_option = input('piedra, papel o tijeras => ')

    computer_option = random.choice(options)

    return user_option, computer_option

while user_wins != 2 and computer_wins != 2:

    game_stats(rounds, user_wins, computer_wins)

    user_option, computer_option = player_options_selection()

    print("*" * 10)

    print("Opcion de user: ", user_option)

    print("opcion de computer:", computer_option)

    fight = user_option + computer_option

    print("Resultado: ")

    if user_option == computer_option:
        print('Empate!')

    elif fight in win:
        print("gana user")
        user_wins +=1

    else:
        print("gana computer")
        computer_wins +=1

    print("*" * 10)

    rounds +=1

if user_wins > computer_wins:
    print("Ganar user")

else: 
    print("gana computer")
    
'''

if user_option == computer_option:
    print('Empate!')

elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('user gano!')
    else:
        print('Papel gana a piedra')
        print('computer gano!')

elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel gana a piedra')
        print('user gano')
    else:
        print('tijera gana a papel')
        print('computer gano!')

elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('user gano!')
    else:
        print('piedra gana a tijera')
        print('computer gano!')

'''