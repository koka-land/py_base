def v2(x):
    s = '01'
    o = ''
    while x > 0:
        o = s[x % 2] + o
        x //= 2
    return o

ans = []

for N in range(1, 1000):
    if N % 2 == 0:
        if N % 3 == 0:
            R = int('1' + v2(N)[:-2] + '11', 2)
        else:
            R = int('10' + v2(N) + '0', 2)
        if R > 999:
            ans.append(R)

print(min(ans))

