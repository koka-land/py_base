def v2(x):
    a = '01'
    s = ''
    while x > 0:
        s = a[x % 2] + s
        x //= 2
    return s

for n in range(1, 201):
    r = v2(n)
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += v2((n % 3) * 3)
    if int(r, 2) >= 200:
        print(n)
        break