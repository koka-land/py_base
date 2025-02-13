for a in range(1, 500):
    f = 0
    for x in range(1, 510):
        for y in range(1, 510):
            if ((x % a == 0) <= ((not(x % 55 == 0)) <= (not(y % 101 == 0)))) == 0:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)
        break