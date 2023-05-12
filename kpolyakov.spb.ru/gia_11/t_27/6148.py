'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6148
'''

# Программа для файла А
sp = list(map(int, open('files/27-141a.txt').read().split()))
n, m = sp[0], sp[1]
max_count = 0
count = 0

for j in range(2, n):
    count = 0
    w = m
    for i in range(j, n):
        if w - sp[i] >= 0:
            count += 1
            w -= sp[i]
        else:
            break
    max_count = max(count, max_count)

print(max_count)

# Программа для файла B
sp = list(map(int, open('files/27-141b.txt').read().split()))
n, m = sp[0], sp[1]

w = 0
max_count = 0
start = j = 2
while j < n:
    if w + sp[j] <= m:
        w += sp[j]
        j += 1
    else:
        max_count = max(max_count, j - start)
        w -= sp[start]
        start += 1

print(max_count)