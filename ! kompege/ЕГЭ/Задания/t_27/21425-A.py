f = open('files/27_A_21425.txt')

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

cl = [[], []]
for i in f:
    x, y = map(float, i.split())
    if y < 10:
        cl[0].append([x, y])
    else:
        cl[1].append([x, y])

centers = []
for i in cl:
    centers.append(center(i))
print(centers)
ans1 = int(((centers[0][0] + centers[1][0]) / 2) * 10000)
ans2 = int(((centers[0][1] + centers[1][1]) / 2) * 10000)
print(ans1, ans2)