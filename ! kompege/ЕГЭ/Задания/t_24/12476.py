import time
start_time = time.time()
f = open('files/24_12476.txt')
s = f.readline()
sp_ro = []


start = 0
max_len = 0

for i in range(s.count('RO')):
    sp_ro.append(s.index('RO', start))
    start = s.index('RO', start) + 1

for i in range(len(sp_ro) - 21):
    slice = s[sp_ro[i]:sp_ro[i + 21]]

    if slice.count('ROR') == 0 and \
       slice.count('ORO') == 0:
        max_len = max(max_len, sp_ro[i + 21] + 1 - sp_ro[i])

print(max_len)
end_time = time.time()
print(end_time - start_time)
