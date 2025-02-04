for a in range(1, 1000):
    f = 0
    for x in range(1, 1000):
        g = ((x % a == 0) <= ((x % 28 != 0) or (x % 42 == 0)))
        if g == 0:
            f = 1
            break
    if f == 0:
        print(a)
        break