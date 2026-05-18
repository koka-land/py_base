f = open('files/27_A_29979.txt')
cl = [[], []]

for i in f:
    x, y = map(float, i.split())
    if y < 15:
        cl[0].append([x, y])
    else:
        cl[1].append([x, y])

print('Количество звезд в кластерах: 1 -', len(cl[0]), '2 -',len(cl[1]))

from math import *

c_cl = [[], []]
for i in range(2):
    min_s = 10**10
    for star_alpha in cl[i]:
        s = 0
        for star in cl[i]:
            s += dist(star_alpha, star)
        if s < min_s:
            min_s = s
            c_cl[i] = star_alpha
print('Центр 1 кластера:', c_cl[0])
print('Центр 2 кластера:', c_cl[1])

a1 = 0
for i in cl[0]:
    if i[0] <= 6.010521:
        a1 += 1
print('A1 =', a1)
print('A2 =', int(dist(c_cl[0], c_cl[1]) * 10000))
