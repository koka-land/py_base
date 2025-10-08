for a in range(200):
    fl = 1
    for x in range(210):
        for y in range(210):
            if ((5 < y) or (x > 32)  or (x + 2 * y < a)) == 0:
                fl = 0
                break
        if fl == 0:
            break
    if fl == 1:
        print(a)
        break