import random

options = ("piedra", "papel", "tijera")

win = ("piedratijera", "tijerapapel", "papelpiedra")

user_option = input('piedra, papel o tijera => ')

computer_option = "piedra"

user_wins = 0

comuputer_wins = 0

fight = user_option + computer_option

while user_wins or comuputer_wins < 4:
    rounds = 1

    print("Ronda", rounds,": ")

    if user_option == computer_option:
        print('Empate!')

    elif fight in win:
        print("gana user")
        user_wins +=1

    else:
        print("gana computer")
        comuputer_wins +=1

    
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