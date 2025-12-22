from itertools import product

ans = 0
s = '0123456789ABCDEF'

for i in product(s, repeat=4):
    num = ''.join(i)
    if num[0] != '0':
        if num.count('3') == 1:
            f = 0
            for j in s:
                if j*2 in num:
                    f = 1
                    break
            if f == 0:
                ans += 1

print(ans)
