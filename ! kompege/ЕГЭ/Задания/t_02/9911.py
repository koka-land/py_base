print('x y w z F G')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = int((x or (not(y))) and (not(x == z)) and w)
                g = int((x <= y) and (y <= z) and (z >= w))
                print(x, y, w, z, f, g)