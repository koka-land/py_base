'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''

from itertools import *

def f(x, y, z, w):
    return ((z <= w) or (y == w)) and ((x or z) == y)
for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table=[(0, 1, 1, 0), (a1, 1, 0, a2), (0, a3, a4, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
