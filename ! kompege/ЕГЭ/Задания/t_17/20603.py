f = open('files/17_20603_20603.txt')
sp = []
max5 = 0
ans = 0
max_ans = 0

for i in f:
    sp.append(int(i))
    if int(i) % 10 == 5:
        max5 = max(max5, int(i))

for i in range(len(sp) - 2):
    c2 = 0
    s3 = 0
    for j in range(3):
        if len(str(sp[i + j])) == 5:
            c2 += 1
        s3 += sp[i + j]
    if c2 == 2 and s3 > max5:
        ans += 1
        max_ans = max(max_ans, s3)

print(ans, max_ans)
