from itertools import product

a = 'БГДНОУШ'
p = 0
pos = 0

for b1, b2, b3, b4, b5, b6 in product(a, repeat=6):
    p += 1
    s = b1 + b2 + b3 + b4+ b5 + b6
    if p % 2 != 0:
        if s[0] != 'Б':
            if s.count('Н') >= 2:
                if s.count('У') == 0:
                    pos = p

print(pos)
