def v2(x):
    a = '0123456789ABCDEF'
    s = ''
    while x > 0:
        s = a[x % 2] + s
        x //= 2
    return s

otvet = 0

for n in range(1, 50):
    r = v2(n)
    #r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '11' + r[2:] + '0'
    else:
        r = '10' + r[2:] + '1'
    r = int(r, 2)
    otvet = max(otvet, r)

print(otvet)