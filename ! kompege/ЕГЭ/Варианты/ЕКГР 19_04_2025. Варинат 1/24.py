s = open('files/24.txt').readline()
qfg = []
start = 0
nomer = 0
min_len = len(s)

for i in range(s.count('QFG')):
    qfg.append(s.index('QFG', start))
    start = s.index('QFG', start) + 1
    if len(qfg) >= 105:
        s_qfg = s[nomer:qfg[-1]+3:]
        if s_qfg.count('QFG') == 105:
            min_len = min(min_len, len(s_qfg))
        nomer = qfg[i - 105] + 1

print(min_len)

