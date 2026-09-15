from itertools import product
s = 'АЕКНТЦ'
s1 = 'АЕК'
n = 0

for i in product(s, repeat=5):
    n += 1
    w = ''.join(i)
    if (n % 2 == 0) and w[0] not in s1 and w.count('Т') > 0:
        print(n)
        break