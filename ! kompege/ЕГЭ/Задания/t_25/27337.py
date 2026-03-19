def d(x):
    sp = []
    while x % 2 == 0:
        sp.append(2)
        x //= 2
    div = 3
    while div ** 2 <= x:
        while x % div == 0:
            sp.append(div)
            x //= div
        div += 2
    if x > 1:
        sp.append(x)
    return sp

count = 0
for i in range(123456789, 10**10):
    sp = d(i)
    if len(sp) == 7 and str(sum(sp)).count('5') == 1 and str(max(sp))[-1] == '9':
        print(i, max(sp))
        count += 1
    if count == 5:
        break