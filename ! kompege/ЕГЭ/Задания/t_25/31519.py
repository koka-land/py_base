def mnoj(x):
    sp = []

    while x % 2 == 0:
        sp.append(2)
        x //= 2
    d = 3
    while d ** 2 <= x:
        while x % d == 0:
            sp.append(d)
            x //= d
        d += 2
    if x > 1:
        sp.append(x)
    return(sp)

ans = []
for i in range(1103285719, 10**12, 2):
    p = mnoj(i)
    if len(p) == 2:
        if str(p[0]).count('16') == 1 and str(p[1]).count('16') == 1:
            ans.append([i, p[0]])
    if len(ans) == 5:
        break
for i in ans:
    print(i)