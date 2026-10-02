f = dict()
f[1] = 1

for i in range(2, 3039):
    f[i] = i * f[i - 1]
print((f[3038] + 5 * f[3037]) / f[3036])
