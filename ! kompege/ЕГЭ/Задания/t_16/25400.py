g = {}
f = {}

for n in range(1, 31060):
    if n < 28:
        g[n] = 3 * n - 4
    else:
        g[n] = g[n - 5] - 15

for n in range(31060, 3, -1):
    if n >= 31054:
        f[n] = 3 * (g[n - 2] - 15)
    else:
        f[n] = f[n + 4] + 3020

print(f[15])