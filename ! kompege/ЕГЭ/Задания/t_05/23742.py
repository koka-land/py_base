for n in range(1, 210):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n % 3) * 3)[2:]
    r = int(r, 2)
    if r >= 200:
        print(n)
        break

