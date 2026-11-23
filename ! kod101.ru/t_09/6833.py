f = open('files/9_6833.csv')

ans = 0
ns = 0

for line in f:
    ns += 1
    l = list(map(int, line.split(';')))
    l.sort()
    if len(set(l)) == 4:
        if (l[0] + l[3]) ** 2 > l[1] ** 3 + l[2] ** 3:
            ans += ns

print(ans)