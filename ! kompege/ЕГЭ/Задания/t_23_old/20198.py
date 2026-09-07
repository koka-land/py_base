def f(s, e, a):
    if s == e and a < 3:
        return 1
    elif s > e + 3 or a == 3:
        return 0
    return f(s - 1, e, a + 1) + f(s + 5, e, 0) + f(s * 2, e, 0)

print(f(5, 34, 0))
