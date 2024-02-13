'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4619
'''

a = 11 * 15**65 + 18 * 15**38 + 14 * 15**17 + 19 * 15**11 + 18338
sp = []

while a > 0:
    sp.append(a % 15)
    a = a // 15
sp = list(set(sp))

print(len(sp))
