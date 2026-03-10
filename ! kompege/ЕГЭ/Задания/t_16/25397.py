f = {}
g = {}

for n in range(301220, -100, -1):
    if n >= 301208:
        g[n] = 10 * n + 50
    else:
        g[n] = g[n + 7] - 21

for n in range(1, 2030):
    if n > 40:
        f[n] = f[n - 4] + 3020
    else:
        f[n] = 3 * (g[n - 2] - 15)

print(f[2026])