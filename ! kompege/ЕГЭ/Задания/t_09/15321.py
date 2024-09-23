f = open('files/9_15321.csv')

ans = 0

for i in f:
    sp = list(map(int, i.split(';')))
    sp.sort()
    if sp[3] < sp[0] + sp[1] + sp[2]:
        s = sum(sp)
        f = 0
        for n1 in range(len(sp) - 1):
            for n2 in range(n1 + 1, len(sp)):
                if sp[n1] + sp[n2] == s - (sp[n1] + sp[n2]):
                    f = 1
        if f == 1:
            ans += 1

print(ans)

