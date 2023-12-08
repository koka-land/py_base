f = open('files/24_11954.txt')

s = f.readline().split('Y')

for i in s:
    x = []
    if i.count('X') >= 500:
        x.append(i.index('X'))
        for ix in range(i.count('X') - 1):
            x.append(i.index('X', x[-1] + 1))
        min_x = 10**30
        for j in range(len(x) - 500):
            min_x = min(min_x, x[j + 500] - x[j])

print(min_x)