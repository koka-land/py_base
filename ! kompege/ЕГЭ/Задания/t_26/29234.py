f = open('files/26_29234.txt')
k = int(f.readline())
comp =[0] * k
n = int(f.readline())
profit = [0] * k
client = 0
sp = []
for i in f:
    sp.append(list(map(int, i.split())))
sp.sort()
for i in sp:
    start = i[0]
    end = i[1]
    for j in range(k):
        if comp[j] < start:
            comp[j] = end
            t = end - start
            profit[j] += t * (t + 1) // 2
            client += 1
            break
print(client)
print(max(profit))
