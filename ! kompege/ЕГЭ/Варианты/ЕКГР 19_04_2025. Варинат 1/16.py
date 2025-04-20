sp = []

for n in range(20):
    sp.append(n)

for n in range(20, 33449):
    sp.append((n - 4) * sp[n - 6])

print((sp[33448] - 230 * sp[33442]) // sp[33436])
