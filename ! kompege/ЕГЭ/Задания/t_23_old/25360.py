def f(start, end):
    if start == end: return 1
    if start < end or start == 36: return 0
    return f(start - 3, end) + f(start - 6, end) + f(start // 2, end)

print(f(86, 53) * f(53, 12))
