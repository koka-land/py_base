f = open('files/9_17863.csv')
c = 0

for i in f:
    sp = list(map(int, i.split(';')))
    p = [i for i in sp if sp.count(i) == 3]
    np = [i for i in sp if sp.count(i) == 1]
    if len(p) == 3 and len(np) == 3 and sum(p)**2 > sum(np)**2:
        c += 1

print(c)