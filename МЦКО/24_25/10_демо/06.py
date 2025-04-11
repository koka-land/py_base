from itertools import product

s = 'АВЕНС'
n = 0

for i in product(s, repeat=4):
    n += 1
    w = ''.join(i)
    if w.count('Е') == 0 and w.count('АА') == 0:
        print(n)
        break
