print('x y w z F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((z <= w) and y and (not(x)))
                print(x, y, w, z, int(f))