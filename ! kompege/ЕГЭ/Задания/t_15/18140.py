for a in range(1, 200):
    f = 0
    for x in range(1, 200):
        for y in range(1, 200):
            if ((x - y >= 39) or (y <= x) or (y >= a - 20)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)