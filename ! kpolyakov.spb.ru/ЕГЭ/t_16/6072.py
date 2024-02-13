'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6072
'''

sp = []
count = 0

for i in range(0, 200000001):
    if i == 0:
        sp.append(0)
    else:
        sp.append(sp[-1] + 2 * i)
    if (i >= 100000000) and (sp[i] % 3 != 0):
        count += 1

print(count)
print(int((200000000 - 100000000) / 3) + 1)
#Каждое 3 значение функции не кратно трем