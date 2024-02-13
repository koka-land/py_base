'''
https://inf-ege.sdamgia.ru/problem?id=7986
'''

from itertools import product

k = 0

for x in product('ЗИМА', repeat=5):
    s = ''.join(x)
    if s[0] in 'ЗМ' and s[-1] in 'ИА':
        k += 1

print(k)
