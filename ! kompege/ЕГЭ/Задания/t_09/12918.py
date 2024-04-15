min_sum = 10**10

with open('files/9_12918.csv') as f:
    for i in f:
        sp = list(map(int, i.split(';')))
        sp_set = set(sp)
        if len(sp_set) == 4:
            para = 0
            for num in sp_set:
                if sp.count(num) == 2:
                    para += 1
            if para == 2:
                if sp.count(max(sp)) == 1:
                    if max(sp) * min(sp) > sum(sp) - max(sp) - min(sp):
                        min_sum = min(min_sum, sum(sp))
                        break

print(min_sum)

