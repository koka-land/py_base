'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6719
'''

from itertools import product

s = 'АГМНСТУ'
nomer = 0

for c1, c2, c3, c4, c5, c6 in product(s, repeat=6):
    if c1 != 'У':
        slovo = c1 + c2 + c3 + c4 + c5 + c6
        nomer += 1
        if slovo.count('М') == 2 and slovo.count('Г') <= 1:
            ans = nomer

print(ans)
