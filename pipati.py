import random

options = ("piedra", "papel", "tijera")

win = ("piedratijera", "tijerapapel", "papelpiedra")

rounds = 1

user_wins = 0

computer_wins = 0

while user_wins != 2 and computer_wins != 2:

    print("*" * 10)

    print("Ronda", rounds, ": ")

    print("*" * 10)

    print("Victorias de user: ", user_wins, "/ 2")

    print("Victorias de computer: ", computer_wins, "/ 2")

    print("*" * 10)

    print("Elige una opcion: ")

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    while not user_option in options: 
        print("Elige una opcion valida: ")
        user_option = input('piedra, papel o tijera => ')
        user_option = user_option.lower()

    computer_option = random.choice(options)

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
    print("Gana user")

else: 
    print("gana computer")