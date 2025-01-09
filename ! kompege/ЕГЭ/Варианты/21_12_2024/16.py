sp = [0, 1, 2, 3, 4]
for i in range(5, 13767):
    sp.append(2 * i * sp[i - 4])
print((sp[13766] - 9 * sp[13762]) // sp[13758])