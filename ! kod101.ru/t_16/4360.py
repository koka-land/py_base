f = dict()
f[1] = 1
for n in range(2, 30):
    f[n] = n * f[n - 1]

print((f[3038] + 5*f[3037]) // f[3036])