g = {}
f = {}
for n in range(248065, -100, -1):
    if n >= 248045:
        g[n] = n / 20 + 28
    else:
        g[n] = g[n + 9] - 4

for n in range(1, 674):
    if n >= 19:
        f[n] = f[n - 4] + 3580
    else:
        f[n] = 6 * (g[n - 7] - 36)

print(int(f[673]))
