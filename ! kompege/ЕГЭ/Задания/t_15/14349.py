print('a b c F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (c <= ((b and (not(a))) <= (not(c))))
            print(a, b, c, int(f))