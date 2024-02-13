max_sum = 0

for n in range(3, 10):
    s = '5' + '3' * n

    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    summa = 0
    for j in s:
        summa += int(j)
    max_sum = max(max_sum, summa)

print(max_sum)