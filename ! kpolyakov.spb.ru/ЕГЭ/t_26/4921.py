'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4921
'''

f = open('files/26-73.txt')
sp = []
sp_r = []
n = int(f.readline())

for i in f:
    sp.append(list(map(int, (i.split()))))

sp.sort()
max_count = 0
num_r = 0

i = 0
while i < n:
    if len(sp_r) == 0:
        sp_r.append(sp[i][1])
        num_r = sp[i][0]
        i += 1
    else:
        if sp[i][0] == num_r:
            sp_r.append(sp[i][1])
            i += 1
        else:
            if len(sp_r) > 1:
                sp_r = list(set(sp_r))
                sp_r.sort()
                count = 1
                for j in range(1, len(sp_r)):
                    if sp_r[j] - 2 == sp_r[j - 1]:
                        count += 1
                    else:
                        if count > max_count:
                            max_count = count
                            num = num_r
                        count = 1
            sp_r = []

print(max_count, num)


