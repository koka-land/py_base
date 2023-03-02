'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6058
'''

f = open('files/24-247.txt', 'r')
maxdl = 1
maxcount = 1
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in f:
    for j in s:
        ps = j
        while ps in i:
            ps = ps + j
        if len(ps)-1 > maxdl:
            maxdl = len(ps)-1
            maxcount = i.count(j)
        if len(ps)-1 == maxdl:
            if i.count(j) > maxcount:
                maxcount = i.count(j)

print(maxcount)
