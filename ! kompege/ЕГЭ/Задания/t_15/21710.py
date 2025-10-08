print('a b c f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a, b, c, int((not(a)) <= (b == c)))