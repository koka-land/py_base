print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((z == w) and (x <= y) or (not(w)))
                if f == 0:
                    print(x, y, z, w, int(f))