def f(s, e):
    if s == e:
        return 1
    if s < e or s == 24:
        return 0
    if s > 9:
        return f(s - 1, e) + f(int(s**0.5), e) + f(s // 10, e)
    else:
        return f(s - 1, e) + f(int(s**0.5), e)

print(f(602, 7))





