f = open('files/27_B.txt', 'r')
sum = 0
min = 10 ** 10

n = f.readline()

for i in f:
    sp = sorted(list(map(int, i.split())))
    sum = sum + sp[2]
    if ((sp[2] - sp[0]) < min) and ((sp[2] - sp[0]) % 91 != 0):
        min = sp[2] - sp[0]
    if ((sp[2] - sp[1]) < min) and ((sp[2] - sp[1]) % 91 != 0):
        min = sp[2] - sp[1]

if sum % 91 != 0:
    print(sum)
else:
    print(sum - min)