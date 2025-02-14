def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return (s)

for n in range(1, 300):
    r = v3(n)
    if sum([int(i) for i in r]) % 2 == 0:
        r = '12' + r[2:] + '0'
    else:
        r = '10' + r[2:] + '2'
    if int(r, 3) > 105:
        print(n)
        break
