f = open('files/EGE_26_25363.txt')
n = int(f.readline())
o = []
a = []
c = [0] * n
for i in f:
    sp = list(map(int, i.split()))
    o.append(sp[0])
    a.append(sp[1])
r = o + a
r.sort()
up = 0
down = 0
for i in r:
    if i in o:
        pos = o.index(i)
    else:
        pos = a.index(i)
    if c[pos] == 0:
        c[pos] = 1
        if o[pos] < a[pos]:
            up += 1
        else:
            down += 1
    if c.count(0) == 1:
        break
print(c.index(0) + 1)
print(down)