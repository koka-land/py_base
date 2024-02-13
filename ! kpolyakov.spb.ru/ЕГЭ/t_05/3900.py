'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3900
'''

for i in range(99, 1000):
    r = bin(i)[2:]
    for j in range(3):
        if r.count('0') == r.count('1'):
            r += r[-1]
        else:
            if r.count('1') < r.count('0'):
                r += '1'
            else:
                r += '0'
    if int(r, 2) % 4 == 0:
        print(i)
        break
