def perevod(x, ss):
    s = '0123456789ABCDEF'
    res = ''
    while x > 0:
        res = s[x % ss] + res
        x = x // ss
    return res

min_n = 10000
min_r = 10000
for n in range (1, 100):
    n1 = bin(n)[2::]
    n2 = perevod(n, 2)
    #print(n1, n2)
    sum1 = 0
    sum2 = 0
    sum1 = n1.count('1')
    for i in n2:
        sum2 = sum2 + int(i)
    #print(sum1, sum2)
    if sum1 % 2 == 0:
        n1 = n1 + '0'
        n1 = '1' + n1[2::]
    else:
        n1 = n1 + '1'
        n1 = '11' + n1[2::]
    r = int(n1, 2)

    if (r > 25) and (r < min_r):
        min_r = r
        min_n = n
print(min_n)
