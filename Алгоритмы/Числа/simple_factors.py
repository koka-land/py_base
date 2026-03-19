def simply_factors(a):
    s_f = []
    while a % 2 == 0:
        s_f.append(2)
        a //= 2
    f = 3
    while f ** 2 <= a:
        while a % f == 0:
            s_f.append(f)
            a //= f
        f += 2
    if a > 1:
        s_f.append(a)
    return s_f

a = int(input())
print(a, simply_factors(a))