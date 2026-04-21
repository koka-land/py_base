def mn(x):
    sp = []
    while x % 2 == 0:
        sp.append(2)
        x //= 2

    div = 3
    while div ** 2 <= x:
        while x % div == 0:
            sp.append(div)
            x //= div
        div += 2

    if x > 1:
        sp.append(x)
    return sp

ans1 = []
ans2 = []
for i in range(8996453, 10**10):
    sp = mn(i)
    if len(sp) == 2:
        if str(sp[0]).count('3') == 2 and str(sp[1]).count('3') == 2:
            ans1.append(i)
            ans2.append(sp[1])
    if len(ans1) == 5:
        break
for i in range(5):
    print(ans1[i], ans2[i])