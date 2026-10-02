g = dict()
for n in range(1510, -10, -1):
    if n > 1500:
        g[n] = 5
    else:
        g[n] = g[n + 1] + g[n + 2] +1
f = dict()
for n in range(0, 1210):
    if n <= 4:
        f[n] = 1
    else:
        f[n] = f[n - 1] + f[n - 3] + g[n - 2]

print((f[1200] + g[100]) % 10000)