ans = []
for n in range(40):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r, 2)
    if r < 19:
        ans.append(n)
print(max(ans))