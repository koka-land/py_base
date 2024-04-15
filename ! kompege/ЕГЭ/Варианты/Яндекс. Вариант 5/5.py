from itertools import product
c = '123456789'

for i in product(c, repeat=4):
    n = ''.join(i)
    t = 0
    sp = []
    r = ''
    for i in n:
        t += int(i)
    for i in n:
        sp.append(t % int(i))
    sp = sorted(sp, reverse=True)
    for i in sp:
        r += str(i)
    if int(r) > 2000:
        print(n)
        break
