f = open('files/9_31355.csv')

ans = 0

for i in f:
    sp = list(map(int, i.split(';')))
    sp_c = [sp.count(i) for i in sp]
    if sp_c.count(3) == 3 and sp_c.count(1) == 3:
        p1, p2 = 1, 1
        for i in range(len(sp)):
            if sp_c[i] == 1:
                p1 *= sp[i]
            else:
                p2 *= sp[i]
        if p2 < p1:
            ans += 1

print(ans)