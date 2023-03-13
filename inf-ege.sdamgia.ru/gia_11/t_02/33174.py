'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''

from itertools import*

def f(x,y,z,w):
    return ((x<=y)==(w<=x))and(z<=w)

for a1,a2,a3,a4 in product([0,1],repeat=4):
    table=[(1,0,0,1),(1,a1,a2,0),(a3,0,1,a4)]
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r)))for r in table]==[1,1,1]:
                print(p)