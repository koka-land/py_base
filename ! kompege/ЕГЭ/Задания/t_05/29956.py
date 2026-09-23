def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

for n in range(1, 200):
    r = v3(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + v3((n % 3) * 5)
    r = int(r, 3)
    if r >= 177:
        print(n)
        break