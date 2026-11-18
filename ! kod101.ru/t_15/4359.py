for a in range(1, 900):
    fl = 0
    for x in range(1, 910):
        f = ((x % a == 0) or ((70 <= x <= 90) <= (x % 22 != 0)))
        if f == 0:
            fl = 1
            break
    if fl == 0:
        print(a)