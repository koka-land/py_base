'''
https://inf-ege.sdamgia.ru/problem?id=16033
*by Aldoshin Nikita
'''

for i in range(0,200):
    b = bin(i)[2::]
    b = str(b)
    if i % 2 == 0:
        b = b + '01'
    else:
        b = b + '10'
    r = int(b,2)
    if r > 102:
        print(r)
        break
