def f(c1, c2, h):
    if (c1 + c2 >= 180) and (h == 4):
        return 1
    if (c1 + c2 >= 180) and (h != 4):
        return 0
    if (c1 + c2 < 180) and (h == 4):
        return 0
    else:
        if h % 2 != 0:
            return f(c1 + 2, c2, h + 1) or \
                   f(c1, c2 + 2, h + 1) or \
                   f(c1 + c2, c2, h + 1) or \
                   f(c1, c1 + c2, h + 1)
        else:
            return f(c1 + 2, c2, h + 1) and \
                   f(c1, c2 + 2, h + 1) and \
                   f(c1 + c2, c2, h + 1) and \
                   f(c1, c1 + c2, h + 1)

for i in range(1, 181):
    if f(18, i, 1) == 1:
        print(i)
