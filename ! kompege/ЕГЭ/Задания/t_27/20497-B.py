f = open('files/27.19.B_20497.txt')
clusters = [[], [], [], [], []]
stars = [[], [], [], [], []]

for i in f:
    x, y = map(float, i.split())
    if y > 40:
        if x > -40 and x < -20:
            clusters[1].append([x, y])
        elif x > -15:
            clusters[3].append([x, y])
    else:
        if x < -35:
            clusters[0].append([x, y])
        elif x > -30 and x < -10:
            clusters[2].append([x, y])
        elif x > 0:
            clusters[4].append([x, y])

for i in range(5):
    max_ = 0
    for star in clusters[i]:
        sum_ras = 0
        for j in clusters[i]:
            sum_ras += ((j[0] - star[0]) ** 2 + (j[1] - star[1]) ** 2) ** 0.5
        if sum_ras / (len(clusters[i]) - 1) > max_:
            stars[i] = star
            max_ = sum_ras / (len(clusters[i]) - 1)

Tx = Ty = 0

for i in stars:
    Tx += i[0]
    Ty += i[1]

print(int((Tx / 5) * 10000), int((Ty / 5) * 10000))