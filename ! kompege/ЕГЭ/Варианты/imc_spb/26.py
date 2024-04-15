f = open('files/26_6641.txt', 'r')
sp = []
sp_s = []
sp_check = []
count = 0
items = 0

n, m = f.readline().split()
n = int(n)
m = int(m)

for i in f:
    sp.append(i.split())
    sp[len(sp)-1][0] = int(sp[len(sp)-1][0])

for i in sp:
    if i[1] == 'S':
        sp_s.append(i)

sp.sort()
sp_s.sort()

for i in sp:
    if m - i[0] > 0:
        items += 1
        if i in sp_s:
            sp_s.remove(i)
        sp_check.append(i)
        m = m - i[0]
        if i[1] == 'S':
            count += 1
    else:
        break

sp_check.sort(reverse=True)

for i in sp_check:
    if i[1] == 'W':
        if m + i[0] - sp_s[0][0] > 0:
            m = m + i[0] - sp_s[0][0]
            count += 1
            sp_s.pop(0)
        else:
            break

print(count, m)