f = open('files/17_29349.txt')
sp = []
min123 = 10**10
for i in f:
    sp.append(int(i))
    if abs(sp[-1]) % 123 == 0 and sp[-1] > 0:
        min123 = min(min123, sp[-1])

ans1 = 0
ans2 = []

for i in range(len(sp) - 1):
    s = sp[i] + sp[i + 1]
    if s < min123:
        ans1 += 1
        ans2.append(s)

print(ans1)
print(abs(max(ans2)))
