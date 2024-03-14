f = open('files/9_2047.csv')
count = 0

for i in f:
    sp = list(map(int, i.split(';')))
    if (sp[0] == sp[2]) and (sp[0] + sp[1] == 180):

        count += 1

print(count)