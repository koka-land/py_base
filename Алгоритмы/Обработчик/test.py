f = 1
while f == 1:
    try:
        a = int(input())
        f = 0
    except ValueError:
        print('Неправильный ввод, введите число цифрами!')

print(a)