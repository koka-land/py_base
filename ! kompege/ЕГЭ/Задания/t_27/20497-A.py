f = open('files/27.19.A_20497.txt')
clusters = [[], [], []]
stars = [[], [], []]

for i in f:
    x, y = map(float, i.split())
    if x < 0 and y < 0:
        clusters[0].append([x, y])
    elif y > 1 and y < 7 and x > -1 and x < 2:
        clusters[1].append([x, y])
    elif x > 0.5 and y < 0 and y > -5:
        clusters[2].append([x, y])

for i in range(3):
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

print(int((Tx / 3) * 10000), int((Ty / 3) * 10000))