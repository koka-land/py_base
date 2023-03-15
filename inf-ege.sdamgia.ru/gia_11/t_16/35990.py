'''
https://inf-ege.sdamgia.ru/problem?id=35990
*by Aldoshin Nikita
'''

def f(x):
    if x == 0:
        return 0
    if x > 0 and x % 2 == 0:
        return f(x/2)
    if x % 2 !=0:
        return 1 + (f(x - 1))
k = 0
for i in range(1,500):
    if f(i) == 3:
        k += 1
    print(k)