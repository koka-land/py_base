print('y x w z F')
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                F = ((w <= (y == z)) and (y == (z <= x)))
                if F == 0:
                    print(y, x, w, z, int(F))