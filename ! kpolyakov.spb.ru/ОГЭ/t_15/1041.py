'''
https://kpolyakov.spb.ru/school/oge/gen.php?action=viewTopic&topicId=1041
'''

n = int(input())
max_ = 0

for i in range(n):
    a = int(input())
    if (a > max_) and (a % 10 == 3):
        max_ = a

print(max_)
