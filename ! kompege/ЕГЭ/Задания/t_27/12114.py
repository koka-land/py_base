f = open('files/27A_12114.txt')
k = int(f.readline())
n = int(f.readline())
sp = []

for i in f:
    sp.append(int(i))

max_price = 0

for p1 in range(0, n - 2 * k):
    for p2 in range(p1 + k, n - k):
        for p3 in range(p2 + k, n):
            max_price = max(max_price, sp[p1] + sp[p2] + sp[p3])

print(max_price)
