f = open('files/26_7602.txt')
s = []
count = 0
k = int(f.readline())
n = int(f.readline())

for i in f:
    s.append(list(map(int, i.split())))

s.sort()
sp = [0] * k

for i in range(n):
    for j in range(len(sp)):
        if s[i][0] > sp[j]:
            sp[j] = s[i][1]
            count += 1
            num = j
            break

print(num+1)
print(count)