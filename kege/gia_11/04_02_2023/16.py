def F(n):
    if n < 3:
        return 1
    if (n > 2) and (n % 2 == 0):
        return F(n - 1) + 2 * n - 1
    if (n > 2) and (n % 2 != 0):
        return F(n - 2) + 2 * n


print(F(21) - F(19))
