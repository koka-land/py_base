print('a b c F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (((not b) and c) <= (((not a) and c) <= b))
            print(a, b, c, int(f))