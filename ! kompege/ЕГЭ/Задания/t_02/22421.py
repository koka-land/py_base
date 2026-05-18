print('x w y z f')
for x in range(2):
    for w in range(2):
        for y in range(2):
            for z in range(2):
                a = (not(z <= y))
                b = (x == w)
                f = (not(a or (b) or x))
                if f == 1:
                    print(x, w, y, z, int(f))
