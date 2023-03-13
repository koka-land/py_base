'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5993
'''

for i in range(10, 100, 2):
    s = '>2' + '12'*i + '<'

    while not('>2<' in s):
        s = s.replace('>1', '>2', 1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('1<', '<2', 1)

    sum = 0
    s1 = '012345789'
    for j in s:
        if j in s1:
            sum += int(j)

    if sum > 103:
        print(i)
        break