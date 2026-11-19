print('a b c d F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((c <= (not d)) and a and (not b))
                if f == 1:
                    print(a, b, c, d, int(f))