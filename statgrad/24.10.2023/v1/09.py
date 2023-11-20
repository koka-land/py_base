f = open('../files/09.csv')
count = 0

for i in f:
    sp = set(map(int, i.split(';')))
    if len(sp) == 6 and (max(sp) + min(sp)) / 2 > (sum(sp) - max(sp) - min(sp)) / 4:
        count += 1
print(count)