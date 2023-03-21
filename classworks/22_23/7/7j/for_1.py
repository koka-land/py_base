'''
Программа сложения n чисел
'''
n = int(input('Введите количество чисел: '))
summ = 0
proiz = 1
for i in range(n):
    a = int(input('Введите число: '))
    summ += a
    proiz *= a
print('Сумма:', summ)
print('Произведение:', proiz)
