f = open('files/17_12926.txt')
sp = []
count = 0
max4 = -10**10
max2 = -10**10
min_sum = 10*10

for i in f:
    sp.append(int(i))

for i in range(len(sp) - 3):
    if abs(sp[i]) % 10 == \
       abs(sp[i + 1]) % 10 == \
       abs(sp[i + 2]) % 10 == \
       abs(sp[i + 3]) % 10:
        max4 = max(max4, sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3])

for i in sp:
    if (i >= 10) and (i <= 99) or (i >= -99) and (i <= -10):
        max2 = max(max2, i)

for i in range(len(sp) - 4):
    count_min = 0
    for j in range(5):
        if sp[i + j] < max4:
            count_min += 1
    if count_min == 1:
        if (sp[i] + sp[i+1] + sp[i+2]+ sp[i+3] + sp[i+4]) % max2 == 0:
            count += 1
            min_sum = min(min_sum, sp[i] + sp[i+1] + sp[i+2]+ sp[i+3] + sp[i+4])

print(count, min_sum)