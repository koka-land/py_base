'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''

from itertools import *

def f(x, y, z, w):
    return ((w <= y) and (not(y) == x)) and (x or z)

for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(a1, 1, 1, 1), (1, 1, a2, a3), (a4, a5, a6, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
