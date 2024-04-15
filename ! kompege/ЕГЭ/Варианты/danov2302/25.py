for i in range(10101011, 10**10):
    if i % 2023 == 0:
        a = i
        break

for i in range(a, 10**10, 2023):
    s = str(i)
    if s[0] == '1' and s[2] == '1' and s[4] == '1' and s[6] == '1' and s[-1] == '1':
        sum = 0
        for j in s:
            sum += int(j)
        if sum == 22:
            print(i)