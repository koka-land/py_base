f = open('files/27_A_18314.txt')

c = [[], []]
r = [[], []]

for i in f:
    x, y = map(float, i.split(' '))
    if x < 23:
        c[0].append([x, y])
    else:
        c[1].append([x, y])

for i in range(len(c)):
    for j in range(len(c[i])):
        ras = 0
        for k in range (len(c[i])):
            ras += abs(c[i][k][0] - c[i][j][0]) + abs(c[i][k][1] - c[i][j][1])
        r[i].append(ras)

x1 = c[0][r[0].index(min(r[0]))][0]
y1 = c[0][r[0].index(min(r[0]))][1]
x2 = c[1][r[1].index(min(r[1]))][0]
y2 = c[1][r[1].index(min(r[1]))][1]

print(int(((x1 + x2) / 2) * 1000))
print(int(((y1 + y2) / 2) * 1000))

