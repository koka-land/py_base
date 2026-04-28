f = open('files/27_A_28946.txt')
clusters = [[], []]
stars = [[], []]

for i in f:
    x, y = map(float, i.split())
    if y < 15:
        clusters[0].append([x, y])
    else:
        clusters[1].append([x, y])

for i in range(2):
    min_ = 10**10
    for star in clusters[i]:
        s = 0
        for j in clusters[i]:
            s += ((j[0] - star[0]) ** 2 + (j[1] - star[1]) ** 2)
        if s  < min_:
            stars[i] = star
            min_ = s

a2 = abs(int((stars[0][0] - stars[1][0]) * 10000))
print(a2)