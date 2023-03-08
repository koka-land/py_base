f = open('files/27_B.txt', 'r')
sum = 0
min = 10 ** 10

n = f.readline()

for i in f:
    sp = sorted(list(map(int, i.split())))
    sum = sum + sp[2]
    min_m = sp[2] - sp[0]
    min_s = (sp[2] - sp[1]
    if (min_m < min) and (min_m % 91 != 0):
        min = min_m
    if (min_s < min) and (min_s % 91 != 0):
        min = min_s

if sum % 91 != 0:
    print(sum)
else:
    print(sum - min)
