f = open('files/9.csv')

count = 0

for i in f:
    sp = list(map(int, i.split(';')))
    if sp.count(min(sp)) > 1:
        count += 1
    else:
        mn = set(sp)
        f = 0
        if len(mn) == 4:
            for i in mn:
                if sp.count(i) == 3:
                    f = 1
        if f == 1:
            count += 1

print(count)