f = open('files/9_16375.csv')

count = 0

for i in f:
    sp = list(map(int, i.split(';')))
    if len(set(sp)) == 6:
        sp2 = []
        for j in sp:
            if sp.count(j) == 2:
                a = j * j
            else:
                sp2.append(j)
        sp2.sort()
        b = sp2[0] * sp2[1] * sp2[2]
        if b > a:
            count += 1

print(count)
