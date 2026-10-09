f = open('files/9_31506.csv')
ans = 0
for i in f:
    a = list(map(int, i.split(',')))
    if len(a) == len(set(a)):
        a.sort()
        if 2 * (a[0] + a[-1]) > sum(a[1:-1]):
            ans += 1
print(ans)