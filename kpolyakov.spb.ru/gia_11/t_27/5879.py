'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5879
'''

f = open('files/27-129b.txt', 'r')
sp = []
max_sum = 0
n = int(f.readline())

for i in f:
    sp.append(int(i))

for st in range (n-1):
    ost_n = [0] * 13
    ost_s = [0] * 13
    summ = 0
    for i in range(n):
        summ = summ + sp[i]
        ost = summ % 13
        if ost == 0:
            if (summ > max_sum) and ((i+1) % 13 == 0):
                max_sum = summ
        else:
            if ost_n[ost] == 0:
                ost_n[ost] = i + 1
                ost_s[ost] = summ
            else:
                if summ - ost_s[ost] > max_sum:
                    if (((i+1) - ost_n[ost]) + 1) % 13 == 0:
                        max_sum = summ - ost_s[ost]
    sp.append(sp[0])
    sp.pop(0)

print(max_sum)
print(summ)

