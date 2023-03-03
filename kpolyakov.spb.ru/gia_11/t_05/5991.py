def inv(x):
    res = ''
    for i in x:
        if i == '0':
            res = res + '1'
        else:
            res = res + '0'
    return res

min_n = 0
min_r = 10**10

for n in range(64, 500):
    r = bin(n)[2::]
    if r.count('1') % 2 == 0:
        r = int(r[:-4:] + inv(r[-4::]), 2)
    else:
        r = int(r[:-5:] + inv(r[-5:-1:]) + r[-1], 2)
    if r < min_r:
        min_r = r
        min_n = n

print(min_n)