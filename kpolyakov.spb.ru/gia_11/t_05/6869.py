'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6869
'''

maxi = 0

for i in range(1000, 10000):
    k = []
    m = []
    K = ''
    M = ''
    for j in range(4):
        k.append(str(i)[j])
        m.append(str(i)[j])
    k.sort(reverse=True)
    m.sort()
    for j in range(4):
        K = K + str(k[j])
        M = M + str(m[j])
    K = int(K)
    M = int(M)
    if K - M == 6174 and K > maxi:
        n = i
        maxi = K

print(n)