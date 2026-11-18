for a in range(1, 1000):
    fl = 0
    for x in range(1, 1050):
        f = (((405 % x == 0) <= (81 % x == 0)) or (a - x > 162))
        if f == 0:
            fl = 1
            break
    if fl == 0:
        print(a)
        break