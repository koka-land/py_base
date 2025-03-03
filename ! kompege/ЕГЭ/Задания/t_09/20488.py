f = open('files/9.22_20488.csv')
ans = 0

for i in f:
    sp = list(map(int, i.split(';')))
    l = [i for i in sp if sp.count(i) == 1]
    if sum(l) >= (sum(sp) - sum(l)) * 3 and 0 < len(l) < len(sp):
        ans += 1

print(ans)
