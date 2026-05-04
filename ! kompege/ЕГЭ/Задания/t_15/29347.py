print('A B C')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (not(a)) <= ((b) == (c))
            print(a, b, c, int(f))
