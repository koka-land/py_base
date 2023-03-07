from itertools import *


def f(x, y, w, z):
    return not ((w or not (y)) and x) or (y == z)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 1, a1, 0), (1, 1, 0, a2), (a3, 1, a4, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
