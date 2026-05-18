f = open('files/27_B_21425.txt')

def dist(s1, s2):
    d = ((s1[0] - s2[0])**2 + (s1[1] - s2[1])**2)**0.5
    return d

def center(x):
    min_s = 10**10
    for star in x:
        s = 0
        for i in x:
            s += dist(star, i)
        if s < min_s:
            min_s = s
            c = star
    return c

cl = [[], [], []]
for i in f:
    x, y = map(float, i.split())
    if x < 0:
        cl[0].append([x, y])
    elif y < 10:
        cl[1].append([x, y])
    else:
        cl[2].append([x, y])

centers = []
for i in cl:
    centers.append(center(i))

ans1 = int(sum(i[0] for i in centers) / 3 * 10000)
ans2 = int(sum(i[1] for i in centers) / 3 * 10000)

print(ans1, ans2)