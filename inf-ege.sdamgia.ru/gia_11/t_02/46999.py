'''
https://inf-ege.sdamgia.ru/problem?id=46999
'''

from itertools import *

def f(x, y, z, w):
    return (x == (y <= z)) and ((not(w)) <= (x == y))

for a1, a2 in product([0, 1], repeat=2):
    table = [(1, 0, 1, 1), (0, 1, 1, 1),(0, a1, 0, a2)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)