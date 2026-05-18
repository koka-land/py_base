s = 'ДЖОС'
n = 0
from itertools import product
for i in product(s, repeat=6):
    n += 1
    w = ''.join(i)
    if w[:2] == 'ЖС':
        print(n)
        break