f = open('files/27A_7603.txt')
n = int(f.readline())
k = int(f.readline())
sp = []
for i in range(k):
    sp.append(int(f.readline()))

max_l = 0
max_sum = 0

for i in range(len(sp), n):
    a = int(f.readline())
    max_sum = max(max_sum, a + sp[0], a + max_l)
    max_l = max(max_l, sp[0])
    sp.pop(0)
    sp.append(a)

print(max_sum)
