def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x == 81:
        return 0
    else:
        return f(x + int(str(x)[0]), y) + f(x + 3, y) + f(2 * x - 1, y)

print(f(42, 73) * f(73, 89))