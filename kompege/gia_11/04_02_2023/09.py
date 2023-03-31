f = open('files/9.csv', 'r')
count = 0

for i in f:
    x = sorted(list(map(int, i.split(';'))))
    if (x[0] != x[1] != x[2]) and (x[0] + x[1] > x[2]):
        count += 1

print(count)
