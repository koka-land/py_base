'''
https://inf-ege.sdamgia.ru/problem?id=15856
*by Aldoshin Nikita
'''


for a in range(0, 300):
    c = 0
    for x in range(0, 300):
        for y in range(0,300):
            if (y + 2 * x < a) or (x > 15) or (y > 30):
                c+=1
    if c == 90000:
        print(a)
        break
