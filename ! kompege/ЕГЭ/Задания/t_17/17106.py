f = open('files/17_12106.txt')
sp = []
m = 10 ** 10

for i in f:
    sp.append(int(i))
    if int(i) % 117 == 0 and int(i) > 0:
        m = min(m, int(i))

ans = 0
ans2 = 10 ** 10

for i in range(len(sp) - 1):
    if (sp[i] < 0 and sp[i + 1] >= 0) or (sp[i] >= 0 and sp[i + 1] < 0):
        if (sp[i] + sp[i + 1]) % m == 0:
            ans += 1
            ans2 = min(ans2, sp[i]**2 + sp[i + 1]**2)

print(ans, ans2)