def f(x):
    m = set()
    for i in range(1, 101):
        if x % i == 0:
            m.add(i)
    return m

l = '123456789ABCDEFGHIJKLMNO'
ans = set()
for x in l:
    ans = ans.union(f(int('8AF7' + x + '11', 25) + int(x + 'DA87', 25)))

print(len(ans))