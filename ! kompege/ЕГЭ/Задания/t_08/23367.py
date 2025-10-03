from itertools import product

str = '0123456'
no = ['00', '11', '22', '33', '44', '55']
c = 0

for i in product(str, repeat=5):
    num = ''.join(i)
    if num.count('6') == 1 and num[0] != '0':
        e = 0
        for j in no:
            if j in num:
                e = 1
                break
        if e == 0:
            c += 1

print(c)
