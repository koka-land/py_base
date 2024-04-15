'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6029
'''

for n in range(1, 10**10):
    n = str(n)
    b = ''
    for i in n:
        a = bin(int(i))[2::]
        for j in range(len(a), 4):
            a = '0' + a
        if a.count('1') % 2 == 0:
            a = a + '0'
        else:
            a = a + '1'
        b = b + a
    b = int('1' + b[2::] + '0', 2)
    if b == 674890:
        print(n)
        break