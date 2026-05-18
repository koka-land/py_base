f = open('files/26_28945.txt')
n = int(f.readline())
sp = []
for i in f:
    a, b = map(int, i.split())
    b = a + b
    sp.append([a, b])
sp.sort(key =lambda x:(x[1]))

cl = [sp[0]]
for i in sp:
    if i[0] >= cl[-1][1]:
        cl.append(i)

max_end = 0
for i in sp:
    if i[0] >= cl[-2][1]:
        max_end = max(max_end, i[1])
print(len(cl), 10000 - max_end)
