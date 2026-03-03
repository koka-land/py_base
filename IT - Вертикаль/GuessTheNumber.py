#Guess The Number - Угадай число

import random

print('\n    Guess The Number - Угадай числo\n')

print('    Выбери режим игры:')
print('        1 - Игрок загадывает число')
print('        2 - Компьютер загадывает число')
type_game = int(input('    Ваш выбор: '))

dg = [1, 100, 1000, 10000, 10**10]
print('    Выбери уровень:')
print(f'        1 - Легкий     (1 - {dg[1]})')
print(f'        2 - Нормальный (1 - {dg[2]})')
print(f'        3 - Сложный    (1 - {dg[3]})')
print(f'        4 - Ужасный    (1 - {dg[4]})')
dif_game = int(input('    Ваш выбор: '))

if type_game == 1:
    print('error')
elif type_game == 2:
    guess_num = random.randint(1, dg[dif_game])
    print(f'    Я загадал число от 1 до {dg[dif_game]}')
else:
    print('error')
