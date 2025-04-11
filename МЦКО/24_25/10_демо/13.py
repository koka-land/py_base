f = open('files/13.txt')
sp = []
n = 100000
ans = 0
max_sum = -100000

for i in f:
    a = int(i)
    if a < n and abs(a) % 15 != 0:
        n = a
    sp.append(a)

for i in range(len(sp) - 1):
    if sp[i] % n == 0 and sp[i + 1] % n == 0:
        ans += 1
        max_sum = max(max_sum, sp[i] + sp[i + 1])

print(ans, max_sum)