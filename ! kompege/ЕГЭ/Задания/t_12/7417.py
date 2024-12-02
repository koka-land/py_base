f = 0
n = 0

while f == 0:
    n += 1
    s = '>' + '0' * 37 + '1' * n + '2' * 37

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    sum_ = 0
    for i in range(len(s) - 1):
        sum_ += int(s[i])

    kd = 0
    for d in range(2, int(sum_ ** 0.5) + 1):
        if sum_ % d == 0:
            kd += 1
            break
    if kd == 0:
        f = 1

print(n)