from itertools import *

def f(x, y, z, w):
    return (x and (not(z)) and (not(w))) or (x and (not(z)) and y)

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(1, a1, a2, a3), (0, a4, 1, a5), (a6, a7, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)