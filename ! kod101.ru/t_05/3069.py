def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

sp = []

for n in range(1, 2500):
    r = v3(n)
    if n % 3 == 0:
        r = r + r[:3]
    else:
        r = r + v3(sum(int(i) for i in r) * 5)
    r = int(r, 3)
    if r > 2500 and r % 2 != 0:
        sp.append(r)

print(min(sp))
