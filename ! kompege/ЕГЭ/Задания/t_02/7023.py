print('y x w z F')
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                F = (not(((((not(w)) <= (not(y)))) <= (not(z))) <= x))
                print(y, x, w, z, int(F))