'''
https://inf-ege.sdamgia.ru/problem?id=15846
*by Aldoshin Nikita
'''

for i in range(1, 100):
    c = bin(i)[2::]
    if i % 2 == 0:
        c += '00'
    else:
        c += '11'
    r = int(c,2)
    if r > 115:
        print(i)
        break
