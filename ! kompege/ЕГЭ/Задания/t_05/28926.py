def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

ans = []

for n in range(1, 1000):
    r = v3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += v3(sum(int(i) for i in r) * 2)
    r = int(r, 3)
    if r % 2 != 0 and r > 520:
        ans.append(r)

print(min(ans))

