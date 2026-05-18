s = 'АВЕНС'
from itertools import product
n = 0
for i in product(s, repeat=4):
    n += 1
    w = ''.join(i)
    if 'Е' not in w and 'АА' not in w:
        print(n, w)
        break