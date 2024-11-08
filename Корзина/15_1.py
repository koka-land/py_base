for a in range(1, 1000):
    f = 0
    for x in range(1, 1001):
        if ((x % 33 == 0) <= ((x % a != 0) <= (x % 242 != 0))) == 0:
            f = 1
            break
    if f == 0:
        print(a)
