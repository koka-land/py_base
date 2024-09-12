sp = [0, 1]
for i in range(2, 2025):
    sp.append((i - 1) * sp[i - 1])
print((sp[2024] + 2 * sp[2023]) // sp[2022])