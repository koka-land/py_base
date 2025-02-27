f = open('files/9.7_20190.csv')
from itertools import permutations
ans = 0

for s in f:
    l = list(map(int, s.split(';')))
    for j in permutations(l):
        if (j[2] / j[1] == j[1] / j[0]) and (j[2] / j[1]) != 1:
            ans += 1
            break

print(ans)