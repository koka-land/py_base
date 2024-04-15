for start in range(2544301, 10**10):
    if start % 23 == 0:
        break

for i in range(start, 10**8, 23):
    s = str(i)
    if s[0] == '2' and s[2:6] == '5443' and s[-1] == '1':
        print(i, i // 23)