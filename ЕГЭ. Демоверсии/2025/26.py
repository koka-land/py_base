f = open('files/26_17881.txt')
n = int(f.readline())
sp = [list(map(int, i.split())) for i in f if list(map(int, i.split())).count(2) == 0]
sp = sorted(sp, key=lambda x: (-sum(x[1:]), x[0]))
print(sp[n // 4 - 1][0])

f = open('files/26_17881.txt')
sp2 = [list(map(int, i.split())) for i in f if list(map(int, i.split())).count(2) > 2]
sp2 = sorted(sp2, key=lambda x: (-sum(x[1:]), x[0]))
print(sp2[0][0])

