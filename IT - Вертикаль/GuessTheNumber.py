#Guess The Number - Угадай число

import random
game = 1

while game == 1:
    print('\n    Guess The Number - Угадай числo\n')
    print('    Выбери режим игры:')
    print('\n        1 - Игрок загадывает число')
    print('        2 - Компьютер загадывает число')
    print('        0 - Выход')
    type_game = int(input('\n    Ваш выбор: '))

    if type_game in range(1, 3):
        dg = [1, 100, 1000, 10000, 10**10]
        print('\n    Выбери уровень:')
        print(f'\n        1 - Легкий     (1 - {dg[1]})')
        print(f'        2 - Нормальный (1 - {dg[2]})')
        print(f'        3 - Сложный    (1 - {dg[3]})')
        print(f'        4 - Ужасный    (1 - {dg[4]})')
        dif_game = int(input('\n    Ваш выбор: '))

    if type_game == 0:
        game = 0
    elif type_game == 1:
        print('error')
    elif type_game == 2:
        guess_num = random.randint(1, dg[dif_game])
        print(f'    Я загадал число от 1 до {dg[dif_game]}')
        player_num = 0

        while guess_num != player_num:
            player_num = int(input('    Введи число, которое я загадал: '))
            if guess_num > player_num:
                print('\n    Я загадал число больше')
            elif guess_num < player_num:
                print('\n    Я загадал число меньше')
            else:
                print('\n    Ты угадал!')
                input('\n    Нажми Enter для возврата в меню')
    else:
        print('error')
