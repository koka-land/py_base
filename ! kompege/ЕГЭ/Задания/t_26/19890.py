f = open('files/26.3_19890.txt')
n, m = map(int, f.readline().split())
sp = []

for i in f:
    sp.append(int(i))

sp.sort()

for i in range(310, 321):
    if i in sp:
        ny = sp.index(i)
        break

cy = 0
my = 0
cp = 0

for i in range(ny, len(sp)):
    if my + sp[i] <= m and sp[i] <= 320:
        my += sp[i]
        cy += 1
        cp = sp[i]
    if m - my <= 0 or sp[ny] > 320:
        break

for i in range(ny):
    if my + sp[i] <= m:
        my += sp[i]
        cy += 1
        cp = sp[i]
    else:
        break

if (m - my + cp) in sp:
    my += m - my

print(cy, my)
