'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4195
'''

sp = []

for a in range (1, 5000):
    f = 0
    for x in range(1, 5000):
        if (((x % 16 == 0) != (x % 24 == 0)) <= (x % a == 0)) == False:
            f = 1
            break
    if f == 0:
        sp.append(a)

print(max(sp))