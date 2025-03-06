print('y x w z F')
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                F = ((x <= y) and (y <= z) and (z <= w))
                if F == 1:
                    print(y, x, w, z, int(F))