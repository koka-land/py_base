print('z w y x')
for z in range(2):
    for w in range(2):
        for y in range(2):
            for x in range(2):
                f = (((z <= x) <= (x == y)) or (not(w)))
                if f == 0:
                    print(z, w, y, x)