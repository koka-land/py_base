f = open('files/26_14624.txt')
n = int(f.readline())
k, s, m = map(int, f.readline().split())

sp = [[]] * (k + 1)
for i in f:
    a, b = map(int, i.split())
    print(a, b)
    sp[a].append(b)
print(sp[1])
