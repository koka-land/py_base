'''
https://inf-ege.sdamgia.ru/problem?id=10313
'''


from itertools import product

k = 0
for x in product('ABCDX', repeat = 4):
    s = ''.join(x)
    if s.count('X') == 1:
        k += 1
print(k)
