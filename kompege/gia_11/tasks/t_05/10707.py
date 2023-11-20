def v6(x):
    ss6 = '012345'
    r = ''
    while x > 0:
        r = ss6[x % 6] + r
        x //= 6
    return r

sp = []

for n in range(1, 680):
    r = v6(n)
    if n % 3 == 0:
        r = r + r[0:2]
    else:
        r = r + v6((n % 3) * 10)
    r = int(r, 6)
    if r > 680:
        sp.append(r)

print(min(sp))

