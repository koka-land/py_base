for n in range(1, 100):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = r + '1'
        r = '11' + r[2:]
    r = int(r, 2)
    if r < 19:
        ans = n
print(ans)