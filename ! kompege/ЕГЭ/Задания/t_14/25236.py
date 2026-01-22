ans = 0

for p in range(11, 10**10):
    a = 2 * p**3 + 9 * p**2 + 10 * p + 1
    b = 4 * p**4 + 7 * p**3 + 7 * p**2 + 7 * p + 1
    c = 1 * p**2 + 2 * p + 10

    if a + b + c <= 1500000:
        ans = p
    else:
        print(ans)
        break