'''
https://inf-ege.sdamgia.ru/problem?id=3206
'''

from itertools import product

k = 0

for x in product('АКРУ', repeat=5):
    s = ''.join(x)
    k += 1
    if s[0] == 'К':
        break

print(k)


