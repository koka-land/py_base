from random import randint

n = -1
count = 0

while n < 0:
    n = int(input('Введите количество выстрелов: '))
    if n < 0:
        print('Количество выстрелов не может быть отрицательным')

for i in range(n):
    x = randint(-100, 100)
    y = randint(-100, 100)
    if x >= -7 and x <= 5 and y >= -8 and y <= 5:
        count += 1

print('Количество выстрелов:', n)
print('Количество попаданий:', count)