f = open('files/27_B_18314.txt')

c = [[], [], []]
r = [[], [], []]

for i in f:
    x, y = map(float, i.split(' '))
    if x < -10:
        c[0].append([x, y])
    elif x > 20:
        c[1].append([x, y])
    else:
        c[2].append([x, y])

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
x3 = c[2][r[2].index(min(r[2]))][0]
y3 = c[2][r[2].index(min(r[2]))][1]

print(int(((x1 + x2 + x3) / 3) * 1000))
print(int(((y1 + y2 + y3) / 3) * 1000))

