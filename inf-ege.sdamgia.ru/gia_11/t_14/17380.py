'''
https://inf-ege.sdamgia.ru/problem?id=17380
*by Aldoshin Nikita
'''


a = 3 * 216**4 + 2 * 36**6 - 648
s = ''

while a != 0:
    s += str(a % 6)
    a //=6
    s = s[::-1]

print(s.count('5'))