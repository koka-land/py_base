def div(x):
    summa = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            summa.add(i)
            summa.add(x // i)
    return summa

for i in range(1000, 10000):
    summa = sum(div(i))
    if summa % 100 == 23:
        print(i, summa)