print('x1 x2 x3 x4 x5')
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    a = (x1 or (not(x2)) or (not(x3)) or x4 or (not(x5)))
                    b = ((not(x1)) or (not(x2)) or x3 or x4 or x5)
                    c = (x1 or (not(x2)) or (not(x3)) or (not(x4)) or x5)
                    F = (a and b  and c)
                    print(x1, x2, x3, x4, x5, int(F))