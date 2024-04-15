from itertools import product

s = '0123456789AB'
pr = '2357B'
count = 0

for c1, c2, c3, c4, c5, c6, c7, c8 in product(s, repeat=8):
    if c1 != '0':
        if int(c1, 12) % 2 != int(c8, 12) % 2:
            c_pr = 0
            num = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
            for i in pr:
                c_pr += num.count(i)
            if c_pr > 1:
                count += 1

print(count)
