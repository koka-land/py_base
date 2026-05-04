f = open('files/26_17643.txt')
n = int(f.readline())
sp = []
sp_d = []
sr = 0
for i in f:
    sp.append(list(map(int, i.split())))
    sr += sp[-1][1]
sr = sr / n
sp.sort()
for i in sp:
    if i[1] > sr:
        sp_d.append(i)
start = sp_d[0][0]
if sp_d[0][2] == 0:
    c = sp_d[0][1]
    n = 0
    count_ = 1
else:
    c = 0
    n = 1
    count_ = 0

pr = []

for i in range(1, len(sp_d)):
    if sp_d[i][0] == start:
        if sp_d[i][2] == 0:
            count_ += 1
            c += sp_d[i][1]
        else:
            n += 1

    else:
        pr.append([sp_d[i - 1][0], sp_d[i - 1][1], c, count_, n])
        start = sp_d[i][0]
        count_ = 0
        if sp_d[i][2] == 0:
            c = sp_d[i][1]
            n = 0
            count_ = 1
        else:
            c = 0
            n = 1
            count_ = 0

max_pr = pr[0]
for i in pr:
    if i[3] > max_pr[3]:
        max_pr = i
    elif i[2] > max_pr[2]:
        max_pr = i
print(max_pr[2], max_pr[4])












