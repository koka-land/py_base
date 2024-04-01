s = open('files/24.txt').readline()

t = []
maxx = 0

n = 0
for i in range(s.count('T')):
    t.append(s.index('T', n))
    n = s.index('T', n) + 1

for i in range(len(t) - 101):
    if s[t[i]:t[i + 101]].count('U') == 50:
        maxx = max(maxx, t[i + 101] - t[i] -1)

print(maxx)
