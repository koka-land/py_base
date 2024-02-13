'''
https://inf-ege.sdamgia.ru/problem?id=15807
*by Aldoshin Nikita
'''

def f(x, y):

    if x == y:
        return 1
    if x > y or x == 33:
        return 0
    else:
        return f(x + 1, y) + f(x * 2, y)

print(f(3, 16) * f(16, 37))
