f = open('files/9_4342.csv')
ans = 0
for i in f:
    s = list(map(int, i.split(',')))
    if 5 == len(set(s)):
        s.sort()
        if (s[0] + s[4]) * 2 > sum(s[1:4]):
            ans += 1
print(ans)