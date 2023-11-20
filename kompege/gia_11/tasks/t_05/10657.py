def v3(x):
    r = ''
    while x > 0:
        r = str(x % 3) + r
        x //= 3
    return r

n_max = 0

for n in range(1, 100):
    r = v3(n)
    sum = 0
    for j in r:
        sum += int(j)
    if sum % 3 == 0:
        r = '20' + r
    else:
        r = '10' + r
    r = int(r, 3)
    if r < 100 and n > n_max:
        n_max = n

print(n_max)