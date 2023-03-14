'''
https://inf-ege.sdamgia.ru/problem?id=16435
*by Aldoshin Nikita
'''

for n in range(0,12000):
    b = bin(n)[2::]
    b = str(b)
    b = b[:-1]
    if n % 2 != 0:
        b = b + '10'
    else:
        b = b + '01'
    f = int(b, 2)
    if f == 2017:
        print(n)
