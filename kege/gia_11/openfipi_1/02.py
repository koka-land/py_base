from itertools import *

def f(x, y, w, z):
    return not(y <= w) or (x <= z) or not(x)

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, a2, 0, 0), (a3, 1, a4, a5), (a6, 0, 1, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)