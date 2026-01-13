print('W Z Y X F')
for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                f = (w == z) or (not(y <= w)) or (not(x))
                if f == 0:
                    print(w, z, y, x, int(f))