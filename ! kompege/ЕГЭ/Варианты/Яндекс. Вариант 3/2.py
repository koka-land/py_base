print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((1 == w) == (not((w and x) or y))) <= z
                print(w, x, y, z, f)