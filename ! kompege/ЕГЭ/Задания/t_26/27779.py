f = open('files/26_27779.txt')
sp = set()
for i in f:
    sp.add(int(i))
sp = sorted(list(sp), reverse=True)

start = [sp[0]]
for i in range(1, len(sp)):
    if start[0] - sp[i] < 8:
        start.append(sp[i])
    else:
        break

ans1 = 0
ans2 = 0

for i in start:
    first = i
    count = 1
    for j in sp:
        if first - j >= 8:
            count += 1
            first = j
    if count >= ans1:
        ans1 = count
        if first > ans2:
            ans2 = first

print(ans1)
print(ans2)
