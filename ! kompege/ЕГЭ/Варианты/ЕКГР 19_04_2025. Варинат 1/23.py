def f(s, e):
    if s == e: return 1
    if s > e or s == 31: return 0
    return f(s + 3, e) + f(s + 5, e) + f(s * 3, e)

print(f(12, 15) * f(15, 52) * f(52, 80))