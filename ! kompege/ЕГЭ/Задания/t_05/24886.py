for n in range(2, 1000, 2):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += '11'
    else:
        r += bin(n // 5)[2:]
    r = int(r, 2)
    if r > 896:
        print(n)
        break