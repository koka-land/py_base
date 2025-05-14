sp = {}

for n in range(2030, 80, -1):
    if n >= 2025:
        sp[n] = n
    else:
        sp[n] = n * 2 + sp[n + 2]

print(sp[82] - sp[81])