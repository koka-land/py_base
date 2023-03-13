from itertools import *


def f(x, y, w, z):
    return (x == (not (y))) <= ((z <= (not (w))) and (w <= y))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, 1, 0, 1), (0, a1, 0, a2), (a3, a4, a5, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 0, 0]:
                print(p)
