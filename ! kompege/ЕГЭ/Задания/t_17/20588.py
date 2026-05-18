f = open('files/17_20558.txt')
sp = []
min123 = 10**10

for i in f:
    sp.append(int(i))
    if sp[-1] % 1000 == 123 and sp[-1] > 0:
        min123 = min(min123, sp[-1])

ans1 = 0
ans2 = 0
print(min123)

for i in range(len(sp) - 1):
    if abs(sp[i] - sp[i + 1]) <= min123:
        ans1 += 1
        ans2 = max(ans2, abs(sp[i] - sp[i + 1]))

print(ans1)
print(ans2)