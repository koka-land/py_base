'''
https://inf-ege.sdamgia.ru/problem?id=46972
*by Aldoshin Nikita
'''
from collections import Counter

a = 5*343**8 + 4 * 49**12 + 7**14-98
s = ''

while a != 0:
    s = str(a % 7)
    a = a//7
counter = Counter(s)
print(counter)