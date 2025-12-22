from itertools import product

ans = 0
s = '0123456789ABCDEF'

for i in product(s, repeat=5):
    num = ''.join(i)
    if num[0] != '0':
        if '1' in num or '4' in num or '9' in num:
            f = 0
            for j in s:
                if num.count(j) > 2:
                    f = 1
                    break
            if f == 0:
                ans += 1

print(ans)
