proc = []
f = open('files/22_6755.csv')

for i in f:
    x = list(map(int, i.split(';')))
    proc.append(x)

proc_time = [0] * (len(proc) + 1)

for i in proc:
    if i[2] == 0:
        proc_time[i[0]] = i[1]
    else:
        time = []
        for j in range(2, len(i)):
            time.append(proc_time[i[j]])
        proc_time[i[0]] = max(time) + i[1]

print(max(proc_time))
