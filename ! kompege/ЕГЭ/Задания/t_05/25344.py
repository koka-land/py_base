def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

sp = []

for n in range(1, 300):
    r = v3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += v3((sum(int(i) for i in r)) * 3)
    r = int(r, 3)
    if (r > 208) and (r % 2 != 0):
        sp.append(r)

print(min(sp))