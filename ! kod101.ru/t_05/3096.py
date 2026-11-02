def v4(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s

max_n = 0
min_R = 10**10

for n in range(3, 350):
    r = v4(n)
    if sum(int(i) for i in r) % 3 == 0:
        r = r.replace('0', '*').replace('2', '0').replace('*', '2')
        r = '32' + r
    else:
        r = r[0] + '10' + r[3:] + '33'
    r = int(r, 4)
    if r > 320:
        if r <= min_R:
            min_R = r
            max_n = n

print(max_n)










