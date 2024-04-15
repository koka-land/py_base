'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''

from itertools import *

def f(x, y, z, w):
    return (not(y <= x)) or (z <= w) or not(z)

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 0, a2, a3), (0, 1, a4, a5), (1, a6, a7, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
