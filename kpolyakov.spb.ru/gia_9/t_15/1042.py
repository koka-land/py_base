'''
https://kpolyakov.spb.ru/school/oge/gen.php?action=viewTopic&topicId=1042
'''

a = 1
summ = 0

while a > 0:
    a = int(input())
    if (a >= 100) and( a <= 999) and (a % 4 == 0):
        summ += a

print(summ)
