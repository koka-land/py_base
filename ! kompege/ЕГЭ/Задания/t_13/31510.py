def f(s, e):
    if s == e: return 1
    if s > e: return 0
    s_c = str(s)
    if int(s_c[-2]) < int(s_c[-1]):
        s_c = int('1' + s_c[-1] + s_c[-2])
        return f(s + 1, e) + f(int(s_c), e)
    else:
        return f(s + 1, e)

print(f(100, 141))