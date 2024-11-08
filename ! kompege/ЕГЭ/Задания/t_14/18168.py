def v5(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x = x // 5
    return s

maxn = 0
max4 = 0
a = 5**2025 + 5**400
for x in range(10, 70001):
    a1 = a - x
    v = v5(a1)
    if v.count('4') >= max4:
        max4 = v.count('4')
        maxn = x

print(maxn)
