f = open('files/24_17535.txt').readline()
cd = []
icd = 0
for i in range(f.count('CD')):
    cd.append(f.index('CD', icd))
    icd = f.index('CD', icd) + 1

'''maxlen = max(cd[160] + 1, len(f) - cd[-161] - 1)
for i in range(len(cd) - 162):
    maxlen = max(maxlen, cd[i + 161] - cd[i])

print(maxlen)'''

#2 способ
max_len = 0
sp = []
sp.append(f[:cd[160] + 1])
sp.append(f[cd[-161] + 1:])
for i in range(len(cd) - 162):
    sp.append(f[cd[i] + 1:cd[i + 161] + 1])
for i in sp:
    if len(i) > max_len:
        max_len = len(i)

print(max_len)