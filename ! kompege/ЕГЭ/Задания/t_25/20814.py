def f(x):
    sp = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            sp.add(i)
            sp.add(x // i)
    if sum(sp) % 10 == 9:
        return sum(sp)
    else:
        return 0

c = 0

for i in range(500001, 10**10):
    s = f(i)
    if s > 0:
        c += 1
        print(i, s)
    if c == 5:
        break