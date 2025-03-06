#Сравнение двух чисел
a = int(input())
b = int(input())

if a > b:
    print(a, '>', b)
elif a < b:
    print(a, '<', b)
else:
    print(a, '=', b)