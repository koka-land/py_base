a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if (a >= b) and (a >= c):
    print('Число', a, 'наибольшее')
elif (b >= a) and (b >= c):
    print('Число', b, 'наибольшее')
elif (c >= a) and (c >= b):
    print('Число', c, 'наибольшее')