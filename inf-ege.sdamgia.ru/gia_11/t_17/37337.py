'''
https://inf-ege.sdamgia.ru/problem?id=37368
*by Aldoshin Nikita
'''

f = open('files/17_37337.txt')
c = 0
m = 0
l = [int(i) for i in f]

for i in range (len(l) -1):
    for j in range (i+1, len(l)):
        if (l[i] % 160 != l[j] % 160) and (l[i] % 7 == 0 or l[j] % 7 == 0):
            c += 1
            m = max(m, l[i] + l[j])

print(c, m)