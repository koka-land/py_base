f = open('files/9_5126.csv')
count = 0

for i in f:
    s = list(map(int, i.split(';')))
    m = set(s)
    if len(m) == 4:
        c1 = 0
        sum1 = 0
        c3 = 0
        num3 = 0
        for j in m:
            if s.count(j) == 1:
                c1 += 1
                sum1 += j
            if s.count(j) == 3:
                c3 += 1
                num3 += j
        if c3 == 1 and c1 == 3:
            if (sum1 / 3) <= (num3 * 3):
                count += 1

print(count)

