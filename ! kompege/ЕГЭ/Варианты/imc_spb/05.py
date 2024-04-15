def inv(x):
    res = ''
    for i in x:
        if i == '0':
            res = res + '1'
        else:
            res = res + '0'
    return res

for n in range(1, 1000):
    r = int('1' + inv(bin(n)[2::]) + str((str(n).count('0') + 1) % 2), 2)
    if r > 180:
        print(n)
        break
