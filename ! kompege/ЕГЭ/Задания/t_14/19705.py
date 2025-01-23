a = 43**56 + 113**841

for x in range(2005, 0, -1):
    b = a - x
    b2 = ''
    while b > 0:
        b2 = str(b % 4) + b2
        b = b // 4
    if len(b2) % 2 == 0:
        if (b2.count('0') + b2.count('2')) % 2 == 0:
            if b2.count('2') <= 712:
                print(x)
                break


