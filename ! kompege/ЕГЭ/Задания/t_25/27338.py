def divs(n):
    sp = []
    while n % 2 == 0:
        sp.append(2)
        n //= 2

    div = 3
    while div * div <= n:
        while n % div == 0:
            sp.append(div)
            n //= div
        div += 2

    if n > 1:
        sp.append(n)
    return sp

count = 0

for i in range(987654320, 0, -1):
    sp = divs(i)
    if len(sp) == 13 and str(sum(sp)).count('1') == 1:
        print(i, max(sp))
        count += 1
    if count == 5:
        break