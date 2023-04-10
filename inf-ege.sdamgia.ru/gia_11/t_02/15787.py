'''
https://inf-ege.sdamgia.ru/problem?id=15787
*by Aldoshin Nikita
'''

from itertools import*

def f(x,y,z,w):
    return ((x <= y) and (y <= w)) or (z == (x or y))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, a1, a2, 1), (1, a3, a4, a5), (a6, 1, a7, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r)))for r in table] == [0, 0, 0]:
                print(*p)
