s = open('files/24_23762.txt').readline()

ans = 0
sp_y = []
start_y = 0
for i in range(s.count('Y')):
    sp_y.append(s.index('Y', start_y))
    start_y = s.index('Y', start_y) + 1

for i in range(len(sp_y) - 81):
    if s[sp_y[i] + 1:sp_y[i + 81]].count('2025') >= 90:
        ans =  max(ans, len(s[sp_y[i] + 1:sp_y[i + 81]]))

print(max(ans, sp_y[80] - 1, len(s) - sp_y[-81]))
