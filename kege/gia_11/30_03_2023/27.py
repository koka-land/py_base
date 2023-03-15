import math

f = open('files/27_A_6760.txt', 'r')
n = int(f.readline())
min = 10**10

sp = [list(map(int, i.split())) for i in f]

for j in range(n):
    lab = sp[0][0]
    sum = 0
    for i in range(1, n):
        sum += abs(sp[i][0] - lab) * math.ceil(sp[i][1] / 48)
    if sum < min:
        min = sum
    sp.append(sp[0])
    sp.pop(0)

print(min)