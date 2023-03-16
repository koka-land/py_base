'''
https://inf-ege.sdamgia.ru/problem?id=16397
*by Aldoshin Nikita
'''


def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return f(x+1, y) + f(x*2, y) + f(x+3, y)
print(f(2,10) * f(10,14))