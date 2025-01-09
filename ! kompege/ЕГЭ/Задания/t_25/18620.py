def f(x):
    sum_ = 0
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    d = list(d)
    d.sort(reverse=True)
    if len(d) > 1:
        return (d[0] + d[1])
    else:
        return 0

for n in range(112500000, 112550000):
    if f(n) % 10000 == 1214:
        print(n)