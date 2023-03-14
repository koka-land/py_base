'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4886
'''

a = 8 ** 888 + 16 * 16 ** 1616 - 2 ** 444
sp = []

while a > 0:
    sp.append(a % 8)
    a = a // 8

print(sp.count(max(sp)))


