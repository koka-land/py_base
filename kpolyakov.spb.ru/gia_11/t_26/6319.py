'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6319
'''

f = open('files/26-112.txt')
#f = open('files/test.txt')
k, n = map(int, f.readline().split())
sp = []
cells = [0] * k
count = [0] * k
last_time = [0] * k
max_time = 0

for i in f:
    sp.append(list(map(int, i.split())))

sp.sort(key = lambda x: x[0])

for i in sp:
    f = 0
    for j in range(len(cells)):
        if i[0] >= cells[j] and (cells[j] <= 1440):
            last_time[j] = i[0]
            cells[j] = i[0] + i[1]
            count[j] += 1
            f = 1
            break
    if f == 0:
        if min(cells) <= 1440:
            num = cells.index(min(cells))
            max_time = max(max_time, cells[num] - i[0])
            last_time[num] = cells[num]
            cells[num] += i[1]
            count[num] += 1
    if min(cells) >= 1440:
        break

#print(last_time)
#print(cells)
#print(count)
print(max_time, last_time[count.index(max(count))])