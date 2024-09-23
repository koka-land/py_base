sp = [0]
for i in range(1, 1000000000):
    if i % 2 != 0:
        sp.append(sp[i - 1] + 1)
    else:
        sp.append(sp[i // 2])

print(sp.count(3))
