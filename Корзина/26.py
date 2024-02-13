import math

f = open('26_1.txt')
n = f.readline()
cost = 0
sp = []
for i in f:
    if int(i) <= 150:
        cost += int(i)
    else:
        sp.append(int(i))
sp.sort()
if len(sp) % 2 != 0:
    cost += sp[len(sp)//2]
for i in range(len(sp) // 2):
    cost += math.ceil(sp[i] * 0.8) + sp[len(sp)-1 - i]
print(cost, sp[i])
