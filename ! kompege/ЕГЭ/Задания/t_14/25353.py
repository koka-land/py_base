a = 3 * 27**9 + 2 * 27**6 + 27**3

for x in range (1, 27001):
    b = a - x
    kn = 0
    while b > 0:
        if b % 27 == 0:
            kn += 1
        b //= 27
        if kn > 6:
            break
    if kn == 6:
        print(x)
        break