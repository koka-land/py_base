f = open('17_1.txt')
sp = []
for i in f:
    sp.append(int(i))

maxa = 0
for i in sp:
    if i % 10 == 3:
        if i > maxa:
            maxa = i
maxa = maxa**2
maxs = 0
count = 0
for i in range(0, len(sp)-1):
    if (sp[i] % 10 == 3 and sp[i+1] % 10 != 3) or (sp[i] % 10 != 3 and sp[i+1] % 10 == 3):
        if sp[i]**2 + sp[i+1]**2 >= maxa:
            count += 1
            if sp[i]**2 + sp[i+1]**2 > maxs:
                maxs = sp[i]**2 + sp[i+1]**2
print(count, maxs)