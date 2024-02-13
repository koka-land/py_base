'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2617
'''

f = open('files/26.txt', 'r')
s, n = map(int, f.readline().split())
sp = []

for i in f:
    sp.append(int(i))

sp.sort()
count = 0

for i in range(n):
    if s - sp[i] > 0:
        s -= sp[i]
        count += 1
    else:
        pos = i - 1
        s += sp[pos]
        print(count)
        break

max_num = 0

for i in range(pos + 1, n):
    if s - sp[i] >= 0:
        max_num = max(sp[i], max_num)
    else:
        break

print(max_num)

