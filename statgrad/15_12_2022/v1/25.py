for start in range(1263050, 10 ** 9 + 1):
    if start % 3123 == 0:
        break

for i in range(start, 10 ** 9 + 1, 3123):
    s = str(i)
    if s[0:2:] == '12' and s[-2] == '5' and s[-5:-3:] == '63':
        print(i, i // 3123)
