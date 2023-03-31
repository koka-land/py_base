'''

f = open('../files/22.csv')

sp = [0] + [list(map(int, i.split(';'))) for i in f]
time = [0 for i in range(len(sp))]

for i in range(1, len(sp)):
    if sp[i][2] == 0:
        time[i] = sp[i][1]
    else:
        sp_time = []
        for j in range(2, len(sp[i])):

        time[i] = max(sp_time)

print(len(sp), sp)
print(len(time), time)
'''