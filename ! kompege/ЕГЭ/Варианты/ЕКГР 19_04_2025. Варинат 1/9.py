f = open('files/9.csv')
n = 0
ans = 0
for i in f:
    n += 1
    sp1 = list(map(int, i.split(';')))
    sp2 = sorted(sp1)
    if sp1 == sp2:
        if (sp1[0] + sp1[6]) / 2 < (sum(sp1[1:6])) / 5:
            ans = max(ans, n)

print(ans)