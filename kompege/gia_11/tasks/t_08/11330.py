from itertools import product

a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
a = a[::-1]
p = 0

for b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11 in product(a, repeat=11):
    p += 1
    s = b1 + b2 + b3 + b4+ b5 + b6 + b7 + b8 + b9 + b10 + b11
    if s == 'ИНФОРМАТИКА':
        print(p)
        break

