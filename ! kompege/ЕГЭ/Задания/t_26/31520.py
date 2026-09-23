f = open('files/26_31520.txt')
n, p = map(int, f.readline().split())
c = 0
a = dict()
b = []
for i in f:
    time, client, size = i.split()
    time, client, size = list(map(int, time.split(':'))), int(client), int(size)
    a[client] = a.get(client, 0) + size
    if time[0] < 12:
        if c + size <= p:
            c += size
        else:
            b.append(c)
            c = size
b.sort(reverse=True)
print(max(a, key=a.get))
print(b[0] + b[1])
