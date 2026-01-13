print('W Z Y X F')
for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                f = x and ((w <= y) == z)
                print(w, z, y, x, int(f))