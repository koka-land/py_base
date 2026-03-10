def simple(x):
    def_sp = []
    mul = 2

    while x > 1:
        if x % mul == 0:
            x //= mul
            def_sp.append(mul)
        else:
            mul += 2
    return def_sp

count = 0
for i in range(987654144, 0, -1):
    sp = simple(i)
    if len(sp) == 13:
        print(i, max(sp))
        count += 1
    if count == 5:
        break