'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''

from itertools import *

def f(x, y, z, w):
    return ((y <= z) or (not x and w)) == (w == z)
for a1, a2, a3 in product([0, 1], repeat=3):
    table = [(a1, 1, 0, 0), (0, 0, 0, 1), (0, 1, a2, a3)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
