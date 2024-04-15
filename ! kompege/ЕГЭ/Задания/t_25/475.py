def dev(x):
    sp =[]
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            sp.append(i)
            sp.append(x // i)
    return sp

for i in range(224467, 664423, 2):
    sp = dev(i)
    if 5 in sp and 7 in sp and 13 in sp:
        if max(sp) <= 100000 and str(max(sp))[-2:] == '19':
            if 25 not in sp and 49 not in sp and 169 not in sp:
                print(i, max(sp))
