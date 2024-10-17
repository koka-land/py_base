print('y x w z F')
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                F = (y <= x) and not(w) and z
                if F == True:
                    print(y, x, w, z, F)