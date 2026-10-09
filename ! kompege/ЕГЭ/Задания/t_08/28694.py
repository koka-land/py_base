from itertools import product
s = '0123456789AB'
s1 = '02468A'
ans = 0

for i in product(s, repeat=5):
    num = ''.join(i)
    if num[0] != '0':
        if sum(1 for i in num if i in s1) == 2:
            if sum(1 for i in s1 if (i + i) in num) == 1:
                ans += 1
print(ans)











