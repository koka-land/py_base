def f(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return i + x // i
            break
    return 0

c = 0

for n in range(700001, 10**10):
    m = f(n)
    if m % 10 == 4:
        print(n, m)
        c += 1
    if c == 5:
        break