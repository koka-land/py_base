f = open('files/26_13087.txt')
n = int(f.readline())

sp = []

for i in f:
    sp.append(list(map(int, i.split())))

sp.sort()
a = sp[-1]
sp = sorted(sp, key = lambda x: x[1])

sp1 = [sp[0]]
for i in range(n):
    if sp[i][0] >= sp1[-1][1] + 20:
        sp1.append(sp[i])

print(len(sp1), a[0] - sp1[-2][1])