print('y x w z F')
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                F = (w and ((z or y) == (z and x)))
                print(y, x, w, z, int(F))
