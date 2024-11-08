for a in range(1, 200):
    f = 0
    for x in range(1, 200):
        if (((x % 7 != 0) and (x % 13 == 0)) <= (x > a - 40)) == False:
            f = 1
            break
    if f == 0:
        print(a)

        