print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((w <= z) == (x <= (not(y)))) and (x or z))
                print(x, y, z, w, int(F))