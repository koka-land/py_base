f= {}
for n in range(1, 247564):
    if n < 10:
        f[n] = 1
    else:
        f[n] = (n + 3) * f[n - 3]

print((f[247563] // 519 - 477 * f[247560]) // f[247557])