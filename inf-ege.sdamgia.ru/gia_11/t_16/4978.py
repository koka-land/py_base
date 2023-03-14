'''
https://inf-ege.sdamgia.ru/problem?id=4978
*by Aldoshin Nikita
'''

def f(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if x > 2:
        return f(x - 2) * (x - 1)

print (f(8))