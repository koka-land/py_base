def div(x):
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            if (i + x // i) % 10 == 4:
                return 1
            else:
                return 0

c = 0
for i in range(800000, 10**10):
    if div(i) == 1:
        print(i)
        c += 1
    if c == 4:
        break