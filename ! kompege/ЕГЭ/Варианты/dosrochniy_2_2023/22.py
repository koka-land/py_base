f = open('files/22_7622.csv')

proc = []

for i in f:
    proc.append(list(map(int, i.split(';'))))

time =[0] * (len(proc) + 1)

for i in proc:
    if i[2] == 0:
        time[i[0]] = i[1]
    else:
        vr_sp = []
        for j in range(2, len(i)):
            vr_sp.append(time[i[j]])
        time[i[0]] = i[1] + max(vr_sp)

print(max(time))