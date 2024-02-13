for a in range(3000):
    er = 0
    for x in range(4000):
        f = ((x & 114 != 0) or (x & 94 != 0)) <= ((x & 73 == 0) <= (x & a != 0))
        if f == 0:
            er = 1
            break
    if er == 0:
        print(a)
        break