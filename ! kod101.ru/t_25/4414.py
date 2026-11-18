def mn(x):
    sp = []
    while x % 2 == 0:
        sp.append(2)
        x //= 2
    d = 3
    while d**2 <= x:
        while x % d == 0:
            sp.append(d)
            x //= d
        d += 2
    if x != 1:
        sp.append(x)
    return(sp)

ans = 0
for a in range(1103285718, 10**10):
    sp = [i for i in mn(a) if '16' in str(i) and str(i).count('16') == 1]
    if len(sp) == 2 and sp[0] * sp[1] == a:
        print(a, sp)
        ans += 1
    if ans == 5:
        break

