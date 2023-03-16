'''
https://inf-ege.sdamgia.ru/problem?id=7782
*by Aldoshin Nikita
'''

from itertools import product

c=0
for x in product('НРТУ', repeat = 4):
    s = ''.join(x)
    c += 1
    print(c, s)