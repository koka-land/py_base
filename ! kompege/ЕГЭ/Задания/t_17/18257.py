f = open('files/17_18257.txt')
sp = []
for i in f:
    sp.append(int(i))

m = max(sp) % 10
ans = 1
ans2 = 10**10

for i in range(len(sp) - 2):
    if (i + i + 1) % 10 == m:
        ans += 1
        ans2 = min(ans2, abs((sp[i] + sp[i + 1]) - (i + i + 1)))

print(ans, ans2)