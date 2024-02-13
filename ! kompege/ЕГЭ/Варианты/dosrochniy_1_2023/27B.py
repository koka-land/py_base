f = open('files/27B_7603.txt')
n = int(f.readline())
k = int(f.readline())
sp = [int(i) for i in f]

max_l = max_sum = 0

for i in range(k, n):
    max_l = max(max_l, sp[i - k])
    max_sum = max(max_sum, sp[i] + max_l)

print(max_sum)
