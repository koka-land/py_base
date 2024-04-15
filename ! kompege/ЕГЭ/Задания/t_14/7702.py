sp = set()

for y in range(9, 18):
    for x in range(y):
        a = 5 * 18**3 + x * 18**2 + y * 18 + 10
        b = 1 * y**3 + 8 * y**2 + x * y + 7
        sp.add(a + b)

print(len(sp))