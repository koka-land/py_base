def g(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sum(s)
def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    if s < e:
        return f(s + 1, e) + f(g(s), e)

print(f(2, 24))