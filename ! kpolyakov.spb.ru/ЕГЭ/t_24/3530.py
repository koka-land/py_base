'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3530
'''

f = open('files/24-153.txt', 'r')
s = f.readline()
count = 0

for a in range(6, 10):
    for i in range(len(s) - a - 1):
        if s[i] == 'A' and s[i + a] == 'F':
            count += 1

print(count)