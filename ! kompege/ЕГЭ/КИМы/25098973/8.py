import string
from itertools import product

s = string.digits + string.ascii_uppercase[:7]
ch = s[0::2]
ans = 0

for i in product(s, repeat=6):
    num = ''.join(i)
    if num[0] != '0':
        if sum([num.count(x) for x in num]) == 6:
            num1 =''
            for j in num:
                if j in ch:
                    num1 += '0'
                else:
                    num1 += '1'
            if '000' not in num1 and '111' not in num1:
                ans += 1

print(ans)
