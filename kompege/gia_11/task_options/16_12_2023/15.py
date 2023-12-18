for A in range(1, 200):
    f = 0
    for x in range(1, 210):
        for y in range(1, 210):
            if ((x < A) and (y < 2 * A) or (x + 2 * y > 150)) == False:
                f = 1
                break
        if f == 1:
            break
    if x == 209 and y == 209:
        print(A)
        break