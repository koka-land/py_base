'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6074
*by Aldoshin Nikita
'''

from itertools import *

def f(x, y, w, z):
    return (w == y) or ((x or z) and (z or y))

for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    table = [(a1, 1, 1, a2), (a3, a4, 1, a5), (1, a6, a7, a8)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
