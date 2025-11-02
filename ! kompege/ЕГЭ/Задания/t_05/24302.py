def v3(x):
    alph = '012'
    res = ''

    while x > 0:
        res = alph[x % 3] + res
        x //= 3

    return(res)

res = []

for n in range(167, 550):
    r = v3(n)
    sum_ = 0
    for i in r:
        sum_ += int(i)
    if sum_ % 9 == 0:
        r += '2' #r = r + '2'
    else:
        r += v3(sum_ % 9)
    r = int(r, 3)
    res.append(r)

print(min(res))