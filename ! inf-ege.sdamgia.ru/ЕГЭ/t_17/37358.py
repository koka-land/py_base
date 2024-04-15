'''
https://inf-ege.sdamgia.ru/problem?id=37358
*by Aldoshin Nikita
'''

f = open('files/17_37358.txt')
c = 0
m = 0

l = [int(i)for i in f]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i] + l[j]) % 10 == 0:
            c += 1
            m = max(m, l[i] + l[j])
print(c, m)

