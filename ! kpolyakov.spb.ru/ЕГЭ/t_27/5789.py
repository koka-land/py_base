'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5789
'''

from math import ceil

# Программа для файла А
f = open('files/27-127a.txt')
n, m = map(int, f.readline().split())
sp = []
for i in f:
    a, b = map(int, i.split())
    sp.append([a, ceil(b / 50)])

start = count = max_point = 0
points = [sp[0]]
for i in range(1, n):
    if points[start][0] + m >= sp[i][0]:
        points.append(sp[i])
        count += points[i][1]
    else:
        break

max_point = max(max_point, count)
start += 1

while start != (n - 1):
    end = 0
    while points[end][0] + m <= points[start][0]:
        end += 1
    for i in range(len(points), n):
        if points[start][0] + m >= sp[i][0]:
            points.append(sp[i])
        else:
            break
    count = 0
    for i in range(end, len(points)):
        count += points[i][1]

    max_point = max(max_point, count)
    start += 1

print(max_point)
