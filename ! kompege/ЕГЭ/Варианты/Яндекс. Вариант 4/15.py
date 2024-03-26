for a in range(1, 1000):
    for x in range(1, 1020):
        f = (x & 91 == 0) or ((x & 77 == 0) <= (x & a != 0))
        if f == 0:
            break
    if x == 1019:
        print(a)
        break
