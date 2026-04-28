s = 'Y' + open('files/DEMO_24.txt').readline() + 'Y'
sp = []
start = 0

for i in range(s.count('Y')):
    sp.append(s.index('Y', start))
    start = s.index('Y', start) + 1

ans = 0
for i in range(len(sp) - 81):
    d = sp[i + 81] - sp[i] - 1
    if s[sp[i]:sp[i + 81]].count('2025') >= 90:
        ans = max(ans, d)

print(ans)

