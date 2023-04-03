f = open('../files/22.csv')

sp = [0] + [list(map(int, i.split(';'))) for i in f]
time = [[0, 0, 0] for i in range(len(sp))]

for i in range(1, len(sp)):
    if sp[i][2] == 0:
        time[i][0] = sp[i][0]
        time[i][2] = sp[i][1]
    else:
        sp_time = []
        for j in range(2, len(sp[i])):
            a = next(p for p, (x, _, _) in enumerate(time) if x == sp[i][j])
            sp_time.append(time[a][2])
        time[i][0] = sp[i][0]
        time[i][1] = max(sp_time)
        time[i][2] = max(sp_time) + sp[i][1]

count = 0

for i in range (1, len(time)):
    if time[i][1] < 150 < time[i][2]:
        count += 1

print(count)

