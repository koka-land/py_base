sp = []

for i in range(2026):
    if i < 110:
        sp.append(i)
    else:
        sp.append(i + sp[i - 1])

print(sp[2025] - sp[2021])
