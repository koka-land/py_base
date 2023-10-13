sp = set()

for x in range(18):
    for y in range(9, 18):
        if x < y:
            a = 5 * 18**3 + x * 18**2 + y * 18**1 + 10
            b = 1 * y**3 + 8 * y**2 + x * y**1 + 7
            sp.add(a + b)

print(len(sp))