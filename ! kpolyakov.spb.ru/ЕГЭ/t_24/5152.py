'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5152
'''

s = open('files/24-203.txt', 'r').readline()
count = 0

for start in range(len(s) - 2):
    for sym in range(start + 2, len(s)):
        if len(set(s[start:sym + 1])) < 3:
            count += 1
        else:
            break

print(count)