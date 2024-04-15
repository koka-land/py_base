count = 0

for i in range(452022, 10**10):
    m = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            m = j + i // j
            break
    if m % 7 == 3:
        count += 1
        print(i, m)
        if count == 5:
            break
