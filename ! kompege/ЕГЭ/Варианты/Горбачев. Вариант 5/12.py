ans = 0
for n in range(1000):
    s = '7' + '0' * n
    while '700' in s or '100' in s or '000' in s:
        if '700' in s:
            s = s.replace('700', '01', 1)
        if '100' in s:
            s = s.replace('100', '07', 1)
        if '000' in s:
            s = s.replace('000', '1', 1)

    if s.count('7') == 7:
        ans += n

print(ans)