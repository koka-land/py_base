'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6829
'''

for a in range(1, 400):
    for x in range(1, 410):
        if ((a + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == False:
            break
    if x == 409:
        print(a)
        break