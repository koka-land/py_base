'''
https://inf-ege.sdamgia.ru/problem?id=37340
*by Aldoshin Nikita
'''

f = open('files/17_37340.txt')
c = 0
m = 0
l = [int(i) for i in f]

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] - l[j]) % 2 == 0 and (l[i] % 31 == 0 or l[j] % 31 == 0):
            c += 1
            m = max(m, l[i] + l[j])

print(c, m)

