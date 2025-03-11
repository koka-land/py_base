def f(x):
    if x <= 2:
        return x
    else:
        return g(x) + f(x - 2)

def g(x):
    if x <= 2:
        return x
    else:
        return f(x - 1) - g(x - 2)

print(g(15))

#2 способ

g = []
f = []
for x  in range(16):
    if x <= 2:
        g.append(x)
        f.append(x)
    else:
        g.append(f[x - 1] - g[x - 2])
        f.append(g[x] + f[x - 2])

print(g[15])