f = open('files/27-A_12257.txt')
n = int(f.readline())
sp = []

for i in f:
    sp.append(int(i))

max_count = 0

for i in range(n-1):
    sum = 0
    count = 0
    for j in range(i, n):
        sum += sp[j]
        count += 1
        if sum % 113 == 0:
            count_t = count
    max_count = max(max_count, count_t)

print(max_count)