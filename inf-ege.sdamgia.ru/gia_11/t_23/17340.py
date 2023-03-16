'''
https://inf-ege.sdamgia.ru/problem?id=17340
*by Aldoshin Nikita
'''

def f(x,y):
    if x == y:
        return 1
    if x > y or x == 10:
        return 0
    else:
        return f(x+1,y)+f(x*2,y)+f(x+5,y)
print(f(1, 8) * f(8, 16))
