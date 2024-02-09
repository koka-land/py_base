f = open('files/17_12471.txt')
sp = []
c = 0
sum1 = 0
m13 = -9999999999999
for i in f:
    sp.append(int(i))

for i in sp:
    if i % 100 == 13:
        m13 = max(m13, i)

for i in range(len(sp) - 2):
    ch3 = 0
    c2 = 0
    for j in range(3):
        if sp[i + j] % 2 == 0:
            ch3 += 1
    for j in range(3):
        if len(str(sp[i + j])) == 2:
            c2 += 1
    if (ch3 == 3) or (c2 > 0):
        if sp[i] + sp[i + 1] + sp[i + 2] <= m13:
            c += 1
            sum1 += sp[i] + sp[i + 1] + sp[i + 2]

print(c, sum1//c)

