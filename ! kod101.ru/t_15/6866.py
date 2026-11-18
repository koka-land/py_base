for a in range(1, 400):
    fl = 0
    for x  in range(1, 130):
        for y in range(1, 130):
            f = ((x < a) and (y < 3 * a) or (2 * x + y > 129))
            if f == 0:
                fl = 1
                break
        if fl == 1:
            break
    if fl == 0:
        print(a)
        break