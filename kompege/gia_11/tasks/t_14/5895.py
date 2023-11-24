otv = set()

for y in range(9, 16):
    for x in range(y):
        a = 5 * 16**3 + x * 16**2 + y * 16**1 + 12
        b = 8 * y**3 + x * y**2 + x * y**1 + 7
        otv.add(a + b)
print(len(otv))




