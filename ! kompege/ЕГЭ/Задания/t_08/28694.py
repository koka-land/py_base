from itertools import product
s = '0123456789AB'
ans = 0

for i in product(s, repeat=5):
    num = ''.join(i)
    if num[0] != '0':
        if sum(1 for i in range(0, len(s), 2)) == 2:
            if sum(1 for i in s1 if (i + i) in num) == 1:
                ans += 1

print(ans)









