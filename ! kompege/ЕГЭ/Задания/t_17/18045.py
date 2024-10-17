f = open('files/17_18045.txt')
sp = []
k2 = 0
ans1 = 0
ans2 = 10 ** 10

for i in f:
    sp.append(int(i))
    if int(i) // 100 == 0:
        k2 += 1

for i in range(len(sp) - 1):
    if sp[i] % 10 + sp[i + 1] % 10 == k2:
        ans1 += 1
        if sp[i] + sp[i + 1] < ans2:
            ans2 = sp[i] + sp[i + 1]

print(ans1)
print(ans2)