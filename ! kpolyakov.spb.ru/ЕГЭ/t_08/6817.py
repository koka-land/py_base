'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6817
'''

from itertools import product

s16 = '0123456789ABCDEF'
ch16 = '02468ACE'
v = ['101', '010']
count = 0

for c1, c2, c3 in product(s16, repeat=3):
    if c1 != '0':
        s = c1 + c2 + c3
        if s.count(s[0]) == 1 and s.count(s[1]) == 1 and s.count(s[2]) == 1:
            ch = str(int(s[0] in ch16)) + str(int(s[1] in ch16)) + str(int(s[2] in ch16))
            print(s, ch)
            if ch in v:
                count += 1
print(count)

