def f(x):
    div = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            div.add(i)
            div.add(x // i)
    return sum(div)

num = 500000
c = 0

while c < 5:
    num += 1
    r = f(num)
    if r % 10 == 6:
        print(num, r)
        c += 1
