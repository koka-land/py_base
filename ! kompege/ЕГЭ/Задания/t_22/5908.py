f = open('files/22_5908.csv')
proc = dict()
time = dict()
for i in f:
    now = list(map(int, i.split(';')))
    proc[now[0]] = now[1:]
    time[now[0]] = 0

while 0 in time.values():
    for id in proc:
        if proc[id][1] == 0:
            time[id] = proc[id][0]
        else:
            t = [time[i] for i in proc[id][1:]]
            if 0 not in t:
                time[id] = max(t) + proc[id][0] + len(t)
print(max(time.values()))