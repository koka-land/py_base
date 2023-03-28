f = open('../files/09.csv', 'r')
sp = []
sp_all = []
ans = 0

for i in f:
    sp.append(list(map(int, i.split(';'))))

for i in sp:
    sp_all += i

for i in sp:
    for j in i:
        if i.count(j) == 1:
            if sp_all.count(j) == 45:
                ans += 1

print(ans)