from random import randint
def start():
    clrscr()
    print('Угадайка')
    print('Выберите режим:')
    print(' 1 - ИИ угадывает')
    print(' 2 - ИИ загадывает')
    print(' 3 - Настройки игры')
    print(' 0 - Выход')
    return int(input('Ваш выбор: '))
def clrscr():
    print("\033[H\033[J", end="")
def error():
    clrscr()
    input('Вы сделали ошибку в выборе. Для возврата в меню нажмите Enter')

def stop():
    clrscr()
    print('Спасибо за игру!')
    input('Для выхода нажмите ENTER')
    exit()
def game2(s, e):
    clrscr()
    print(f'Хорошо. Я загадал число в диапазоне от {s} до {e}')
    turn = 1
    num_ii = randint(s, e)
    while True:
        num = int(input('Введите число: '))
        if num > num_ii:
            print('Ха-ха! Я загадал число меньше...')
        elif num < num_ii:
            print('Ха-ха! Я загадал число больше...')
        else:
            print(f'Опа! Ты угадал число... Тебе потребовалось {turn} попыток...')
            input('Для возврата в меню нажмите ENTER')
            break
        turn += 1
def setup(m):
    global s
    global e
    if m == 0:
        s = 1
        e = 100
    else:
        s = int(input(f'Введите начала диапазона. Сейчас он равен {s}: '))
        e = int(input(f'Введите конец диапазона. Сейчас он равен {e}: '))
    return s, e

setup(0)
while True:
    v = start()
    if v == 1:
        game1()
    elif v == 2:
        game2(s, e)
    elif v == 3:
        setup(1)
    elif v == 0:
        stop()

    else:
        error()


