f = open('files/26_6759.txt', 'r')
sp = []
n = int(f.readline())
sum = 0

for i in f:
    sp.append(int(i))
    sum += int(i)

sp.sort(reverse=True)
print(sp)

min_sum = 0
max_sum = 0

for i in range(n // 3, n):
    min_sum += sp[i]

for i in range(2, n, 3):
    max_sum += sp[i]

print(min_sum)
print(sum - max_sum)