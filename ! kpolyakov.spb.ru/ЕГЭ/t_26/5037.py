'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5037
'''

f = open('files/26-79.txt')
s, k = map(int, f.readline().split())

sp = []
sp_r = []

for i in f:
    sp.append(list(map(int, i.split())))

sp.sort()
i = 0
max_r = 0
min_n = 0

while i < s:
    if len(sp_r) == 0:
        num_r = sp[i][0]
        sp_r.append(sp[i][1])
        i += 1
    else:
        if sp[i][0] == num_r:
            sp_r.append(sp[i][1])
            i += 1
        else:
            if len(sp_r) > 1:
                sp_r.sort()
                for j in range(1, len(sp_r)):
                    if sp_r[j] - sp_r[j-1] - 1 == k:
                        max_r = num_r
                        min_n = sp_r[j-1] + 1
                        break
            sp_r = []

print(max_r, min_n)
