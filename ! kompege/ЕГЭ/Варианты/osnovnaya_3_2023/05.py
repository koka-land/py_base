def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

max = 0

for n in range(1, 300):
    r = f(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + f((n % 3) * 4)
    r = int(r, 3)
    if r < 199 and n > max:
        max = n
print(max)
