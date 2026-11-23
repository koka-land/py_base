f = open('files/22_6873.csv')
proc = []
for i in f:
    proc.append(list(map(int, i.split(';'))))
time = [0] * (len(proc))
while 0 in time:
    for i in range(len(proc)):
        if proc[i][2] == 0:
            time[i] = proc[i][1]
        else:
            t =  [time[j] for j in [j - 1 for j in proc[i][2:]]]
            if 0 not in t:
                time[i] = max(t) + proc[i][1]

print(sum([1 for i in range(len(proc)) if (time[i] - proc[i][1] <= 6 <= time[i])]))
