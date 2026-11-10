a = 7**170 + 7**100
for x in range(2030, 0, -1):
    b = a - x
    n = 0
    while b > 0:
        if b % 7 == 0:
            n += 1
        b //= 7
    if n == 70:
        print(x)
        break