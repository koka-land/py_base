'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6792
'''

f = open('files/26-130.txt')
sp = []
visitors = []
max_visitors = 0
max_count = 0

for i in f:
    sp.append(list(map(int, i.split())))

sp.sort()

for i in sp:
    flag = 0
    if len(visitors) == 0:
        visitors.append(i[1])
    else:
        if i[0] <= visitors[0]:
            visitors.append(i[1])
        else:

            if i[0] > visitors[0]:
                flag = 1
            visitors.append(i[1])
            while i[0] >= visitors[0]:
                visitors.pop(0)
    if len(visitors) > max_visitors:
        max_visitors = len(visitors)
        max_count = 1
    elif len(visitors) == max_visitors:
        if flag == 1:
            max_count += 1
    visitors.sort()

print(max_count, max_visitors)