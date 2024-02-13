'''
https://kpolyakov.spb.ru/school/oge/gen.php?action=viewTopic&topicId=1041
'''

n = int(input())
count = 0

for i in range(n):
    a = int(input())
    if (a % 6 == 0) and (a % 10 == 4):
        count += 1

print(count)
