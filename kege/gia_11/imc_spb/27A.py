from math import ceil

f = open('files/27A_6638.txt')
n = int(f.readline())
sp = []

for i in f:
    sp.append(list(map(int, i.split())))
    sp[len(sp)-1][1] = ceil(sp[len(sp)-1][1] / 100)

min_energy = 10**10
na = -1

for i in range(n):
    energy = 0
    for j in range(1, n):
        energy += abs(sp[0][0] - sp[j][0]) * sp[j][1]
    if energy < min_energy:
        min_energy = energy
        na = sp[0][0]
    sp.append(sp[0])
    sp.pop(0)

print(na)