f = open('files/26_6641.txt', 'r')
sp = []
sp_s = []
count = 0

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

print(sp_s)

for i in sp:
    if i in sp_s:
        sp_s.remove(i)
    if m - i[0] > 0:
        m = m - i[0]
        if i[1] == 'S':
            count += 1
    else:
        break

print(count)
print(sp_s)


