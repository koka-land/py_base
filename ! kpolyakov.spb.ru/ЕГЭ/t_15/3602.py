'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3602
'''

for a in range(0, 100):
    f = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if ((x - 2 * y < 3 * a) or (2 * y > x) or (3 * x > 50)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)
        break