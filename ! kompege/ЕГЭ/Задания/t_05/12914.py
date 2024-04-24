def v2(x):
    a = '0123456789ABCDEF'
    s = ''
    while x > 0:
        s = a[x % 2] + s
        x //= 2
    return s

otvet = 0

for n in range(1, 200):
    r = v2(n)
    #r = bin(n)[2:]
    if n % 3 == 0:
        r = r.replace('0', '11')
    else:
        r = r.replace('1', '10')
    r = int(r, 2)
    if r <= 161:
        otvet = max(otvet, r)

print(otvet)