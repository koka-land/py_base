import math

f = open('files/27_A_6760.txt', 'r')
n = int(f.readline())
price = [0] * n
ds = us = 0

sp = [list(map(int, i.split())) for i in f]

for i in range(n):
    sp[i][1] = math.ceil(sp[i][1] / 48)
    if i > 0:
        price[0] += (sp[i][0] - sp[0][0]) * sp[i][1]
        ds += sp[i][1]

for i in range(1, n):
    us += sp[i-1][1]
    price[i] = price[i-1] - ds * (sp[i][0] - sp[i-1][0]) + us * (sp[i][0] - sp[i-1][0])
    ds -= sp[i][1]

print(min(price))
