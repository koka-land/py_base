f = open('files/27a_8483.txt')
n = int(f.readline())
k = int(f.readline())
sp = []
max_sum = 0
for i in f:
    sp.append(int(i))
print(len(sp))
for i in range(0, n - 2 * k):
    for j in range(i + k + 1, n - k):
        for l in range(j + k + 1, n):
            max_sum = max(max_sum, sp[i] + sp[j] + sp[l])

print(max_sum)
