for n in range(128, 236):
    r = bin(n)[2:]
    if len(r) < 8:
        r = '0' * (8 - len(r)) + r
    res = ''
    for i in r:
        if i == '1':
            res += '0'в
        else:
            res += '1'
    res = n - int(res, 2)
    if res == 185:
        print(n)
        break