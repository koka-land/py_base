'''
https://inf-ege.sdamgia.ru/problem?id=6306
*by Aldoshin Nikita
'''


def f(x):
    if x <= 2:
        return x
    if x > 2:
        return f(x - 1) * f(x - 2)
print(f(7))