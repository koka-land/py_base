f = open('files/09_6016.csv', 'r')
count = 0

for i in f:
    sp = list(map(int, i.split(';')))
    sp.sort()
    if sp[0] < sp[1] and sp[1] < sp[2]:
        if sp[2]**2 < sp[0]**2 + sp[1]**2:
            count += 1

print(count)