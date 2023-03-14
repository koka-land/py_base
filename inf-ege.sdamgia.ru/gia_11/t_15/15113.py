'''
https://inf-ege.sdamgia.ru/problem?id=15113
*by Aldoshin Nikita
'''

s = 0
for a in range(1,300):
    c = 0
    for x in range(0, 300):
        for y in range(0,300):
            if ((x < a) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= a)):
                c += 1
    if c == 90000:
        s += 1
print(s)
