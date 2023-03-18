f = open ('files/18_6753.csv', 'r')
table = []
table_money = []
table_ww = []
table_wh = []

for i in range(2, 9):
    table_ww.append(list((str(9)+' '+str(i)).split()))
for i in range(13, 18):
    table_ww.append(list((str(18)+' '+str(i)).split()))

for i in range(2, 12):
    table_wh.append(list((str(i)+' '+str(12)).split()))

for i in f:
    table.append(list(map(int, i.split(','))))
    table_money.append(list([0] * len(table[0])))

th = len(table)
tw = len(table[0])
table_money[0][0] = table[0][0]

for i in range(1, tw):
    table_money[0][i] = table_money[0][i-1] + table[0][i]

for i in range(1, th):
    table_money[i][0] = table_money[i-1][0] + table[i][0]

for m in range(2):
    for i in range(1, th):
        for j in range(1, tw):
            sp = list((str(i)+' '+str(j)).split())
            if sp in table_ww or sp in table_wh:
                if sp in table_ww:
                    table_money[i][j] = table_money[i][j-1] + table[i][j]
                else:
                    table_money[i][j] = table_money[i-1][j] + table[i][j]
            else:
                if m == 0:
                    table_money[i][j] = max(table_money[i][j-1], table_money[i-1][j]) + table[i][j]
                else:
                    table_money[i][j] = min(table_money[i][j-1], table_money[i-1][j]) + table[i][j]
    print(table_money[tw-1][th-1])
