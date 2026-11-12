f = dict()
g = dict()

for n in range(22570, 5, -1):
    if n >= 22560:
        g[n] = n / 23 + 33
    else:
        g[n] = g[n + 11] - 4

for n in range(13, 549):
    if n >= 21:
        f[n] = f[n - 8] + 1095
    else:
        f[n] = 10 * (g[n - 7] - 36)

print(f[548])