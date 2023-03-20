f = open('files/26.txt', 'r')
sp = []

for i in f:
    sp.append(i.split())

for i in sp:
    i[0] = int(i[0])

sp.sort(reverse=True)
c = 0
max_b = 0

while len(sp) != 0:
    tz = sp[0][0]
    tc = sp[0][1]
    sp[0] = 0
    cb = 1
    c += 1

    for i in range(1, len(sp)):
        if sp[i][0] + 5 <= tz:
            if sp[i][1] != tc:
                cb += 1
                tz = sp[i][0]
                tc = sp[i][1]
                sp[i] = 0

    if cb > max_b:
        max_b = cb

    while 0 in sp:
        sp.remove(0)

print(max_b, c)
