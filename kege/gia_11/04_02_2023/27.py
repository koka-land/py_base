f = open('files/27_A.txt', 'r')
sum = 0

n = f.readline()

for i in f:
    sp = sorted(list(map(int, i.split())))
    sum = sum + sp[2]

print(sum, sum % 91)
