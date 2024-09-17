def v3(x):
    r = ''
    while x > 0:
        r = str(x % 3) + r
        x //= 3
    return r

max_r = 0
for n in range(1, 100):
    r = v3(n)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r  = r + v3((n % 3) * 5)
    r = int(r, 3)
    if r <= 173:вй
        max_r = max(max_r, r)

print(max_r)
