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

#2 СПОСОБ

k = 0

for s in open('files/9_16375.csv'):
    a = [int(x) for x in s.split(';')]
    a2 = [int(x) for x in a if a.count(x) == 2]
    a1 = sorted([int(x) for x in a if a.count(x) == 1])
    if (len(a2) == 2 and len(a1) == 5) and (a1[0] * a1[1] * a1[2] > a2[0] ** 2):
        k += 1

print(k)
