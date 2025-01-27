f = open('files/27_B_1.csv')
sp = []
for i in f:
    sp.append(list(map(float, i.split(';'))))

med = []
for i in range(len(sp)):
    s = []
    x = sp[i][0]
    y = sp[i][1]
    for j in range(len(sp)):
        s.append(((sp[j][0] - x)**2 + (sp[j][1] - y)**2)**0.5)
    med.append(sum(s) / (len(sp) - 1))
print(sp[med.index((min(med)))])
