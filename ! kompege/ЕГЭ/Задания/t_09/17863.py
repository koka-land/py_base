f = open('files/9_17863.csv')
ans = 0

for i in f:
    sp = list(map(int, i.split(';')))
    sp1 = [x for x in sp if sp.count(x) == 1]
    sp3 = [x for x in sp if sp.count(x) == 3]
    if len(sp1) == len(sp3) and sum(sp3)**2 > sum(sp1)**2:
        ans += 1

print(ans)