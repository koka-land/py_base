from itertools import *

ans = set()

def f1(x, y, w, z):
    return (x or (not y)) <= (w == z)
def f2(x, y, w, z):
    return (x or (not y)) == (z <= w)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(0, a1, 0, 0), (a2, 1, 1, a3), (a4, 0, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if ([f1(**dict(zip(p, r))) for r in table] == [0, 0, a5]) and ([f2(**dict(zip(p, r))) for r in table] == [0, a6, 0]):
                ans.add(p)

print(ans)