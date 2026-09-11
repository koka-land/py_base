print('x y w z F')
for z in range(2):
    for y in range(2):
        for x in range(2):
            for w in range(2):
                f = (((x == (not(y))) <= (not(w <= x))) or (not(z)))
                if f == 0:
                    print(x, y, w, z, int(f))