'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6790
'''

sp = []

f = open('files/26-128.txt')

for i in f:
    sp.append(list(map(int, i.split())))