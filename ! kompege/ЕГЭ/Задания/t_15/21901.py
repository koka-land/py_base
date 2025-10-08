for a in range(200):
    fl = 1
    for x in range(210):
        f = (((x & 52 != 0) and (x & 48 == 0)) <= (x & a != 0))
        if f == 0:
            fl = 0
            break
    if fl == 1:
        print(a)
        break