f = open('files/22_25359.csv')
table = []

for i in f:
    table.append(list(map(int, i.split(';'))))

time = [0]*len(table)
while 0 in time:
    for i in table:
        if time[i[0] - 1] == 0:
            if i[2] == 0:
                time[i[0] - 1] = i[1]
            else:
                mini_time = []
                for j in range(2, len(i)):
                    mini_time.append(time[i[j] - 1])
                if 0 not in mini_time:
                    time[i[0] - 1] = max(mini_time) + i[1]

print(max(time))