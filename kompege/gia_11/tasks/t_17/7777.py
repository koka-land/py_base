f = open('files/17var04_7777.txt')

sp = []
count = 0

for i in f:
    sp.append(int(i))

max_n = max(sp)
min_sum = 10 ** 50

for i in range(len(sp) - 2):
    if sp[i] % 10 != 3 and sp[i + 1] % 10 != 3 and sp[i + 2] % 10 != 3:
        if sp[i]**2 + sp[i + 1]**2 + sp[i + 2]**2 > max_n:
            min_sum = min(min_sum, sp[i]**2 + sp[i + 1]**2 + sp[i + 2]**2)
            count += 1

print(count, min_sum)