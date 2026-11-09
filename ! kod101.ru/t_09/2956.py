f = open('files/9_2956.csv')
ans = 0

for i in f:
    s = list(map(int, i.split(',')))
    s_tri = [n for n in s if 100 <= n <= 999]
    if len(s_tri) >= 3:
        s_5 = [n for n in s if n % 5 == 0]
        if len(s_5) == 0:
            ans += 1
print(ans)