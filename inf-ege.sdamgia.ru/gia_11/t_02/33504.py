'''
https://inf-ege.sdamgia.ru/problem?id=33504
'''

from itertools import*

def f(x, y, z, w):
    return (x == (not(y))) <= ((y and not(z)) or (z and not(w)))

for a1,a2,a3,a4,a5,a6 in product([0,1],repeat=6):
    table=[(0,0,a1,0), (a2,0,a3,0), (a4,a5,a6,0)]
    if len(table) == len(set(table)):
        for p in permutations ('xyzw'):
            if [f(**dict(zip(p, r)))for r in table] == [0,0,0]:
                print(p)