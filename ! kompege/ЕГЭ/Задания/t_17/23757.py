f = open('files/17_23757.txt')

sp = []
min2 = 100

ans1 = 0
ans2 = 0

for i in f:
    sp.append(int(i))
    if len(str(sp[-1])) == 2:
        min2 = min(min2, int(i))

for i in range(len(sp) - 1):
    c2 = 0
    if len(str(sp[i])) == 2: c2 += 1
    if len(str(sp[i + 1])) == 2: c2 += 1
    if c2 == 1:
        if (sp[i] + sp[i + 1]) % min2 == 0:
            ans1 += 1
            ans2 = max(ans2, sp[i] + sp[i + 1])

print(ans1)
print(ans2)