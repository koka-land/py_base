'''
Программа сложения n чисел
'''
n = int(input('Введите количество чисел: '))
summ = 0
for i in range(n):
    a = int(input('Введите число: '))
    summ += a
print('Сумма:', summ)
