s = open('files/24_19254.txt').readline()

fsrq = []

start = 0
for i in range(s.count('FSRQ')):
    fsrq.append(s.index('FSRQ', start))
    start = s.index('FSRQ', start) + 1

ans = []
for i in range(len(fsrq) - 81):
    ans.append(fsrq[i + 81] + 2 - fsrq[i])

print(max(ans))
