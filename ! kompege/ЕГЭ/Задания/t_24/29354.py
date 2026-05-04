s = open('files/24_29354.txt').readline()

bc = []

start = 0
for i in range(s.count('BC')):
    bc.append(s.index('BC', start))
    start = s.index('BC', start) + 1

ans = []
for i in range(len(bc) - 191):
    ans.append(bc[i + 191] - 1 - bc[i] + 1)

print(max(ans))