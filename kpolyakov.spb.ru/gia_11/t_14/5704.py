'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5704
'''

for x in range(0, 130):
    a = 2 * 130**4 + 3 * 130**3 + x * 130**2 + 3 * 130 + 2
    b = 3 * 130**4 + x * 130**3 + 2 * 130**2 + 5 * 130 + 3
    c = a + b
    if c % 23 == 0:
        print(c // 23)
        break
