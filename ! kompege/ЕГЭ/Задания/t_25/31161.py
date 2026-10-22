def div(x):
    sp = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            sp.add(i)
            sp.add(x // i)
    sp = list(sp)
    sp.sort()
    return sp

def prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1

ans = []

for i in range (8117600757, 10**12):
    sp = div(i)
    sp_p = []
    for j in sp:
        if prime(j) == 1:
            sp_p.append(j)
    if len(sp_p) > 1:
        a = max(sp_p) - min(sp_p)
        if prime(a) == 1:
            if str(a).count('1') >= 4:
                ans.append([i, a])
                print(i, a)
    if len(ans) == 5:
        break

for i in ans:
    print(i)
