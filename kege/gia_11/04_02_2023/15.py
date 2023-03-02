for a in range(100):
    f = 0
    for x in range(100):
        for y in range(100):
            if ((x > a) or (y > a) or ((y - 2*x + 12) != 0)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)