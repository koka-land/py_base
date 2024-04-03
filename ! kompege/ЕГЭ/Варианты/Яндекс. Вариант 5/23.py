def f(s, e):
    if s == e:
        return 1
    if s < e:
        return 0
    else:
        if s % 3 == 0:
            return f(s - 1, e) + f(s // 3, e)
        else:
            return f(s - s % 3, e) + f(s // 3, e)

print(f(58, 3))