f = open('../files/18.csv', 'r')

table = []
table_energy = []

for i in f:
    table.append(list(map(int, i.split(';'))))

for i in range(len(table)):
    table_energy.append([])
    for j in range(len(table[i])):
        table_energy[i].append(0)

table_energy[0][0] = table[0][0]

for i in range(1, len(table[0])):
    table_energy[0][i] = table_energy[0][i-1] + table[0][i]

for i in range(1, len(table)):
    table_energy[i][0] = table_energy[i-1][0] + table[i][0]

for i in range(1, len(table[0])):
    for j in range(1, len(table)):
        if j < (len(table[0]) - 1):
            table_energy[i][j] = max(table_energy[i-1][j], table_energy[i][j-1], table_energy[i-1][j-1], table_energy[i-1][j+1]) + table[i][j]
        else:
            table_energy[i][j] = max(table_energy[i - 1][j], table_energy[i][j - 1], table_energy[i - 1][j - 1]) + table[i][j]

stroka = len(table) - 1
stolbec = len(table[0]) - 1

count = 0
dist = []

while (stroka + stolbec != 0):
    if (table[stroka][stolbec]) % 2 != 0:
        count += 1
    tz = table_energy[stroka][stolbec] - table[stroka][stolbec]
    dist.append(tz)
    coord = [[n, x.index(tz)] for n, x in enumerate(table_energy) if tz in x]
    if len(coord) == 1:
        stroka = coord[0][0]
        stolbec = coord[0][1]
    else:
        for i in range(len(coord)):
            if (0 <= stroka - coord[i][0] <= 1) and (-1 <= stolbec - coord[i][1] <= 1):
                stroka = coord[i][0]
                stolbec = coord[i][1]

if table[0][0] % 2 != 0:
    count += 1

print(table_energy[len(table)-1][len(table)-1])
print(dist)
print(count)


