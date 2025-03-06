#Определение треугольника
a = int(input())
b = int(input())
c = int(input())

if max(a, b, c) < a + b + c - max(a, b, c):
    print('Треугольник')
else:
    print('Не треугольник')
