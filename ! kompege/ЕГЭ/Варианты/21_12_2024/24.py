s = open('files/24_19254.txt').readline()
sp = []
a = 0
for i in range(s.count('FSRQ')):
    sp.append(s.index('FSRQ', a))
    a = s.index('FSRQ', a) + 1
ans = max(sp[80] + 3, len(s) - sp[-81] - 1)
for i in range(1, len(sp) - 81):
    ans = max(ans, sp[i + 81] - sp[i] + 2)
print(ans)