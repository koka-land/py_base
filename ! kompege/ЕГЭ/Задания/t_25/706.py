num = 0

for i in range(6638225, 6638322, 2):
    count = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            count += 1
        if count > 0:
            break
    if count == 0:
        num += 1
        print(num, i)
