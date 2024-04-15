'''
https://inf-ege.sdamgia.ru/problem?id=18570
*by Aldoshin Nikita
'''

def f(x, y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(1, 14) * f(14, 50))
