for n in range(1, 48):
    r = bin(n)[2:]
    if r.count('0') != 0:
        r = int((r[:r.rfind('0')] + r[:2] + r[r.rfind('0') + 1:])[::-1],     2)
        if r == 123:
            print(n)