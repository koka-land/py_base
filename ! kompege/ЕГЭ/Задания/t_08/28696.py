from itertools import product
s = '0123456789ABCD'
ans = 0

for i in product(s, repeat=5):
    num = ''.join(i)
    if num[0] != '0':
        nech_count = 0
        for n in num:
            if int(n, 14) % 2 != 0:
                nech_count += 1
        if nech_count == 2:
            for n in range(len(num) - 2):
                if int(num[n], 14) % 2 != 0 and num[n] == num[n + 2] and int(num[n + 1], 14) % 2 == 0:
                    ans += 1

print(ans)

