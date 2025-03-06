f = open('files/9.13_19700.csv')
ans = 0

for i in f:
    l = list(map(int, i.split(';')))
    m = set(l)
    if len(m) == 4 and max(l) + min(l) < (sum(l) - max(l) - min(l)):
        ans += 1

print(ans)

