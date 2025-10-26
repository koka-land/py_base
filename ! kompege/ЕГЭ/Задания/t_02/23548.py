print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((x or y) <= z) or (y == w) or z)
                if F == 0:
                    print(x, y, z, w, int(F))
