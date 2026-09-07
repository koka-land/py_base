def f(s, e):
    if s == e: return 1
    if s > e or s == 14: return 0
    return f(s + 1, e) + f(s * 2, e) + f(s * 3, e)

print(f(2, 39))
