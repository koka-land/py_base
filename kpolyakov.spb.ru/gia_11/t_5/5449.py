sp = []
for i in range(1000):
    s = bin(i)[3:]
    if s.count('1') % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '0'
    if int(s, 2) < 450:
        sp.append(int(s, 2))
print(max(sp))
