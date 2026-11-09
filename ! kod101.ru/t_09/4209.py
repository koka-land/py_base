file = open('files/9_4209.csv')
ans = 0

for i in file:
    s = list(map(int, i.split(';')))
    u1 = [s.count(i) for i in s]
    if u1.count(1) == 2 and u1.count(2) == 4:
        u2 = [s[i] for i in range(len(u1)) if u1[i] == 1]
        if (sum(s) - sum(u2)) > sum(u2):
            ans += 1

print(ans)