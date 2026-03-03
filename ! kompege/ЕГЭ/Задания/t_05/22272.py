def v9(x):
    ans = ''
    while x > 0:
        ans = str(x % 9) + ans
        x = x // 9
    return ans

max_n = 0
max_r = 0

for n in range(1, 2900):
    r = v9(n)
    if r[0] == '7':
        r = r.replace('6', '*').replace('3', '6').replace('*', '3')
        r = '34' + r
    else:
        r = r + '45'
        r = '3' + r[1:]
    r = int(r, 9)
    if r >= max_r and r < 2876:
        max_r = r
        max_n = n

print(max_n)
