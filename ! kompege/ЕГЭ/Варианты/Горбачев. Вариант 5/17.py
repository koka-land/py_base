f = open('files/17.txt')

sp = []
m3 = 0
ans = 0
ans2 = 0

for i in f:
    sp.append(int(i))
    if len(str(abs(int(i)))) == 3 and abs(int(i)) % 100 == 33:
        m3 = max(m3, int(i))

for i in range(len(sp) - 2):
    f = 0
    s = 0
    for j in range(3):
        if len(str(abs(sp[i + j]))) == 5 and abs(sp[i + j]) % 100 == 61:
            f = 1
        s += sp[i + j]
    if f == 1 and s >= m3:
        ans += 1
        ans2 = max(s, ans2)

print(ans, ans2)