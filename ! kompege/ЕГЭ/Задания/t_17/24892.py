f = open('files/17_24892.txt')
sp = []
max9 = -100000
ans1 = 0
ans2 = 10**10

for i in f:
    sp.append(int(i))
    if len(str(abs(sp[-1]))) == 4 and sp[-1] < 0 and sp[-1] % 9 == 0:
        max9 = max(max9, sp[-1])

for i in range(len(sp) - 1):
    otr = 0
    if sp[i] < 0: otr += 1
    if sp[i + 1] < 0: otr += 1
    if otr == 1:
        if sp[i] + sp[i + 1] > max9:
            ans1 += 1
            ans2 = min(ans2, sp[i]**2 + sp[i + 1]**2)

print(ans1)
print(ans2)