def mn(x):
    sp_mn = []
    while x % 2 == 0:
        sp_mn.append(2)
        x //= 2
    div = 3
    while div**2 <= x:
        while x % div == 0:
            sp_mn.append(div)
            x //= div
        div += 2
    if x != 1:
        sp_mn.append(x)
    return sp_mn

count = 0
for i in range(2400001, 10**10):
    sp = mn(i)
    if len(sp) == 3 and len(set(sp)) == 3:
        a47 = 0
        for j in sp:
            if str(j).count('4') > 0 or str(j).count('7') > 0:
                a47 += 1
        if a47 == 3:
            print(i, max(sp), sp)
            count += 1
    if count == 5:
        break
