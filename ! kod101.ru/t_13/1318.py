def f(x):
    if x == 3: return 1
    if x < 3 or x == 9 or x == 16: return 0
    return f(x - 1) + f(x - 2) + f(x // 3)

print(f(19))