True = "piedra" and "tijera" or "tijera" and "papel" or "papel" and "piedra"

#lose_scenarios = not(win_scenarios)

user_option = input('piedra, papel o tijera => ')

computer_option = "piedra"

fight = user_option and computer_option

if user_option == computer_option:
    print('Empate!')
elif fight == True
    print("ganas")
else
    print("pierdes")
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
