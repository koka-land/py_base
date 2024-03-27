print('y x z w f')
for y in range(2):
    for x in range(2):
        for z in range(2):
            for w in range(2):
                f = (y <= x) and (not(z)) and w
                if f == 1:
                    print(y, x, z, w, f)