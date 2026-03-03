g = {}
f = {}

for n in range(304000, -1, -1):
    if n > 303728:
        g[n] = n - 15
    else:
        g[n] = g[n + 8] // 2 - 109

for n in range(100, 2050):
    if n >= 128:
        f[n] = f[n - 5] + 1092
    else:
        f[n] = 5 * g[n - 7] + 29

print(f[2049])