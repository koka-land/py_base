'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3530
'''

f = open('files/24-153.txt', 'r')
s = f.readline()
count = 0

for i in range(len(s) - 7):
    if s[i] == 'A' and s[i + 6] == 'F':
        count += 1

for i in range(len(s) - 8):
    if s[i] == 'A' and s[i + 7] == 'F':
        count += 1

for i in range(len(s) - 9):
    if s[i] == 'A' and s[i + 8] == 'F':
        count += 1

for i in range(len(s) - 10):
    if s[i] == 'A' and s[i + 9] == 'F':
        count += 1

print(count)