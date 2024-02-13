'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6816
'''

from itertools import product

s = 'АДУЧ'
gl = 'АУ'
sl = 0

for a1, a2, a3, a4, a5 in product(s, repeat=5):
    o = a1+a2+a3+a4+a5
    if o[0] in gl:
        sl += 1
    if o == 'УДАЧА':
        print(sl)
        break

