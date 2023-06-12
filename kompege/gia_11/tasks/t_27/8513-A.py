f = open('files/27_A_8513.txt')
k = int(f.readline())
n = int(f.readline())
sp = []
for i in f:
    sp.append(int(i))
max_sum = 0
for i in range(n - 4):
    for j in range(i + 4, n):
        max_sum = max(max_sum, sp[i] + sp[j])

print(max_sum)
