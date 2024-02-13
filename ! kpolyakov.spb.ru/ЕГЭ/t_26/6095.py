'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6095
'''

f = open('files/26-104.txt')
sp = []

for i in f:
    sp.append(list(map(int, (i.split()))))

sp.sort()
maxr = 0
maxl = 0

while len(sp) != 0:
    line = 0
    count = 1
    r = sp[0][0]
    sp_r = []
    sp_r.append(sp[0][1])
    sp[0] = 0
    for i in range(1, len(sp)):
        if sp[i][0] == r:
            sp_r.append(sp[i][1])
            sp[i] = 0
        else:
            break
    sp_r = list(set(sp_r))
    sp_r.sort()
    for i in range(len(sp_r) - 1):
        if sp_r[i] + 1 == sp_r[i + 1]:
            count += 1
        else:
            if count >= 5:
                line += 1
            count = 1
    if line >= maxl:
        maxl = line
        maxr = r
    while 0 in sp:
        sp.remove(0)

print(maxl, maxr)