'''
https://inf-ege.sdamgia.ru/problem?id=15632
*by Aldoshin Nikita
'''

a = 4**14 + 2**32 - 4
s = ''

while a != 0:
    s += str(a % 2)
    a //= 2
s = s[::-1]

print(s.count('1'))
