# Программа для файла А
f = open('files/27-B.txt', 'r')
n = int(f.readline())
sp = []
count = 0

for i in f:
    sp.append(int(i))

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if ((sp[i] + sp[j]) % 4 == 0) and ((sp[i] * sp[j]) % 6561 == 0):
            count += 1

print(count)
