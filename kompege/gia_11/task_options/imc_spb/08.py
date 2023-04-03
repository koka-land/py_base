from itertools import *

s = '0123456'
count = 0

for i in product(s, repeat = 5):
    num = ''.join(i)
    if num[0] != '0' and num.count('6') == 1:
        sum_ch, sum_nech = 0, 0
        for j in num:
            if int(j) % 2 == 0:
                sum_ch += int(j)
            else:
                sum_nech += int(j)
        if sum_ch < sum_nech:
            count += 1

print(count)
