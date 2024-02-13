'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5449
'''

for n in range(60, 100):
    r = bin(n)[2::]
    for i in range(3):
        if r.count('0') == r.count('1'):
            r = r + r[-1]
        else:
            if r.count('1') < r.count('0'):
                r = r + '1'
            else:
                r = r + '0'
    if int(r, 2) % 2 == 0 and int(r, 2) % 4 != 0:
        print(n)
        break