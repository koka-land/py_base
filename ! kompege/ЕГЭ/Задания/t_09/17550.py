ans = 0

with open('files/09_17550.csv') as f:
    for i in f:
        n3 = 0
        n3_num = 0
        sp = list(map(int, i.split(';')))
        mn = set(sp)
        if len(mn) == 4:
            for i in mn:
                if sp.count(i) == 3:
                    n3 = 1
                    n3_num = i
            if n3 == 1:
                if (n3_num * 3)**2 > (sum(sp) - n3_num * 3)**2:
                    ans += 1

print(ans)