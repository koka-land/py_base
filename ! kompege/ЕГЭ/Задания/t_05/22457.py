def v7(x):
    r = ''
    s = 0
    while x > 0:
        r = str(x % 7) + r
        s += x % 7
        x //= 7
    return r, s

ans = []
# maxN = 0

for n in range(1, 100):
    r, s = v7(n)
    # print(n, r, s)
    '''s = 0
    for c in r:
        s += int(c)'''
    if s % 2 == 0:
        r += '555'
    else:
        r = '33' + r + '6'
    r = int(r, 7)  #2 - 36
    if r < 12717:
        # maxN = n
        ans.append(n) #добавить в конец списка элемент