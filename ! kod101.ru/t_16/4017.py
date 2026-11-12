g = dict()

for n in range(18, 21):
    g[n] = n + 2
for n in range(21, 37809):
    g[n] = g[n - 3] + 1

print(3 * g[37808] + 7)