def delitel(x):
    sp = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            sp.append(i)
            sp.append(x // i)
    sp = list(set(sp))
    return sp

def nod(a, b, c):
    sp1 = delitel(a)
    sp2 = delitel(b)
    max_del = 1
    for i in sp1:
        if i in sp2:
            max = i
    if max == c:
        return 1
    else:
        return 0

c = 0

for a in range(1, 1001):
    f = 0
    for x in range(1, 1001):
        a_ = nod(a, 420, 2)
        b_ = nod(a, x, 12)
        c_ = nod(110, x, 11)
        if (a_ or ((not(b_)) <= (not(c_)))) == False:
            f = 1
            break
    if f == 0:
        c += 1

print(c)