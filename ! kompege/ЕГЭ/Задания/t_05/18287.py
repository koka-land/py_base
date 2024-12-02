def v3(x):
    s = '01'
    o = ''

    while x > 0:
        o = s[x % 2] + o
        x = x // 2

    return o

ans = []

for N in range(1, 1000):
    #R = bin(N)[2:]
    R = v3(N)
    if len(R) % 2 == 0:
        R = R + '1'
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R > 666:
        ans.append(R)

print(min(ans))