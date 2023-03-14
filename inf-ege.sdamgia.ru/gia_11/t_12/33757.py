'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6111
*by Aldoshin Nikita
'''


for a in range(0,60):
    for b in range(0,60):
        for c in range(0,60):
            s='0'+a*'1'+b*'2'+c*'3'
            while '01' in s or '02' in s or '03' in s:
                s=s.replace('01','30',1)
                s=s.replace('02','101',1)
                s=s.replace('03','202',1)
            if s.count('1')==20 and s.count('2')==10 and s.count('3')==70:
                print(a)
