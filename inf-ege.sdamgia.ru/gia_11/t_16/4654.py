'''
https://inf-ege.sdamgia.ru/problem?id=4654
*by Aldoshin Nikita
'''

def f(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if x == 3:
        return 1
    if x > 3:
        return f(x - 3) + f(x - 2)
    
print(f(10))
