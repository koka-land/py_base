for a in range(1, 200):
    f = 0
    for x in range(1, 210):
        for y in range(1, 210):
            if ((x < a) and (y < (3 * a)) or ((2 * x + y) > 128)) == 0:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)
        break