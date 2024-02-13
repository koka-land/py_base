'''
https://kpolyakov.spb.ru/school/oge/gen.php?action=viewTopic&topicId=1041
'''

n = int(input())
max = 0

for i in range(n):
    a = int(input())
    if (a > max) and (a % 10 == 3):
        max = a

print(max)
