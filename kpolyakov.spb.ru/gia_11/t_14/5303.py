'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5303
'''

a = abs(3*5**1984 - 7*25**777 - 11*125**666 - 404)
count = 0

while a > 0:
    if a % 5 == 2:
        count += 1
    a = a // 5

print(count)