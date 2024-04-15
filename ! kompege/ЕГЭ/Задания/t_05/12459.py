def v4(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s

for n in range(1, 200):
    r = v4(n)
    if len(r) % 2 == 0:
        r = r[0:len(r) // 2] + '0' +r[len(r) // 2:]
    r = int(r)
    if r < 180:
        print(n)