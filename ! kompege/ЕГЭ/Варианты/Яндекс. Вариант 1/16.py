#1 способ
def f(x):
    if x > 10000:
        return 42
    if x % 2 == 0:
        return 2 * x + f(x + 3) + f(x + 4) + f(x + 6)
    else:
        return -(x + f(x + 1) + f(x + 3))

print(f(9996) - f(9994))

#2 способ
sp_i = []
sp_f = []
for i in range(10010, 89, -1):
    sp_i.append(i)
    if i > 10000:
        sp_f.append(42)
    elif i % 2 == 0:
        sp_f.append(2 * i + sp_f[sp_i.index(i) - 3] + sp_f[sp_i.index(i) - 4] + sp_f[sp_i.index(i) - 6])
    else:
        sp_f.append(-(i + sp_f[sp_i.index(i) - 1] + sp_f[sp_i.index(i) - 3]))

print(sp_f[sp_i.index(9996)] - sp_f[sp_i.index(90)])