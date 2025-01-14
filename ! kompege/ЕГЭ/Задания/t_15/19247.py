for A in range(1000):
    fl = 0
    for x in range(1000):
        for y in range(1, 1000):
            f = (x - 3*y < A) or (y > 400) or (x > 56)
            if f == 0:
                fl = 1
                break
        if fl == 1:
            break
    if fl == 0:
        print(A)
        break