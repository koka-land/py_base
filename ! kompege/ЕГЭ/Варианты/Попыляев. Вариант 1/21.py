def f(x, y, z, h):
    l = int((x**2 + y**2 + z**2)**0.5)
    if ((h == 4) or (h == 2)) and (l >= 71):
        return 1
    if (h < 4) and (l >= 71):
        return 0
    if (h == 4) and (l < 71):
        return 0
    else:
        if h % 2 != 0:
            return f(x + 9, y, z, h + 1) or \
                   f(x, y + 9, z, h + 1) or \
                   f(x, y, z + 9, h + 1)
        else:
            return f(x + 9, y, z, h + 1) and \
                   f(x, y + 9, z, h + 1) and \
                   f(x, y, z + 9, h + 1)

for y in range(1, 71):
    if f(19, y, 21, 0) == 1:
        print(y)
