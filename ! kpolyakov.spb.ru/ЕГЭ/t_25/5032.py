'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5032
'''

from itertools import product

s16 = '0123456789ABCDEF'
sp = []

for a, b in product(s16, repeat=2):
    s = (f"1{a}DED{b}BABA")
    if int(s, 16) % int('BA', 16) == 0:
        sp.append(s)

sp.sort(reverse=True)

for i in sp:
    print(int(i, 16), int(i, 16) // int('BA', 16))