def v5(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x //= 5
    return s

sp = []

for n in range(1, 10001):
    r = v5(n)
    if n % 25 == 0:
        r += r[-3:]
    else:
        r += v5(n % 25)
    r = int(r, 5)
    if r > 10000:
        sp.append(n)

print(min(sp))