'''
https://inf-ege.sdamgia.ru/problem?id=4978
*by Aldoshin Nikita
'''

def f(x):
    if x == 1:
        return 1
    if x > 1:
        return f(x - 1) * f(x - 1) - f(x - 1) * x + 2 * x

print(f(4))
