def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s

sp = []

for n in range(1, 101):
    r = v3(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + v3((n % 3) * 4)
    r = int(r, 3)
    if r < 100:
        sp.append(n)

print(max(sp))