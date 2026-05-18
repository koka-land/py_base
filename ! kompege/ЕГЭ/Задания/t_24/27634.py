s = open('files/24_27634.txt').readline()
import time
s1 = time.time()
sp_z = []

start = 0
for i in range(s.count('Z')):
    sp_z.append(s.index('Z', start))
    start = s.index('Z', start) + 1

ans = 10**10

for i in range(len(sp_z) - 269):
    ans = min(ans, sp_z[i + 269] - sp_z[i] + 1)

print(ans)
s1 = time.time() - s1
print(s1)
