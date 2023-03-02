'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4978
'''

f = 0

for i1 in range(15):
    for i2 in range(15):
        for i3 in range(15):
            s = '0' + '1'*i1 + '2'*i2 + '3'*i3 + '0'
            s1 = s
            #print(s1)
            while '00' not in s:
                s = s.replace('01','21022',1)
                s = s.replace('02','310',1)
                s = s.replace('03','230112',1)
            if (s.count('1') == 104) and (s.count('2') == 39) and (s.count('3') == 83):
                print(len(s1))
                print(s1)
                print(s)
                f = 1
                break
        if f == 1:
            break
    if f == 1:
        break
                                                                   
    
