f = open('files/26_17565.txt')
n, s = map(int, f.readline().split())
c = []
for i in f:
    l = list(map(int, i.split()))
    c.append([l[0], l[1] + l[2] + l[3], l[4]])
c.sort(key=lambda x: x[1], reverse=True)

last = c[s - 1][1]
for i in range(s - 1, -1, -1):
    if c[i][1] > last:
        last = c[i][1]
        break

print(last)