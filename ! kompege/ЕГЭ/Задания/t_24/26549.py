s = open('files/24_26549.txt').readline()
sp = []
start = 0
for i in range(s.count('2025')):
    sp.append(s.index('2025', start))
    start = s.index('2025', start) + 1

max_s = 0
for i in range(len(sp) - 51):
    if s[sp[i]:sp[i + 51]].count('Y') >= 140:
        max_s = max(max_s, len(s[sp[i]+1:sp[i + 50]+3]) + 1)

print(max_s)
