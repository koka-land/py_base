sp = []
for a in range(500):
    e = 0
    for x in range(520):
        for y in range(520):
            f = (x + 2 * y > a) or (y < x) or (x < 30)
            if f == 0:
                e = 1
                break
        if e == 1:
            break
    if (x == 519) and (y == 519):
        sp.append(a)

print(max(sp))