def v3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s

#sp = []
ans = 10000000

for n in range(1, 50):
    r = v3(n)
    if n % 3 > 0:
        r = '1' + r + r[-3:]
    else:
        #r = r + v3((r.count('1') + r.count('2') * 2) * 8)
        r = r + v3(sum(int(i, 3) for i in r) * 8)
    r = int(r, 3)
    if abs(1220 - r) < abs(1220 - ans):
        ans = r
    #sp.append(r)
#sp.sort()
#print(sp)
print(ans)



