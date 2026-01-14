s = open('files/24_24977.txt').readline()

pos = []
start = 0

for i in range(s.count('2')):
    start = s.index('2',start)
    if s[start + 2] + s[start + 4] + s[start + 6] == '026':
        pos.append(start)
    start += 1

ans = 0
for i in range(len(pos) - 11):
    if (pos[i + 11] + 6) - (pos[i] + 1) > ans:
        ans = (pos[i + 11] + 6) - (pos[i] + 1)

print(max(pos[11] + 6, ans, len(s) - pos[-11] + 1))
