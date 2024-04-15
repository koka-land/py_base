'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6093
'''

f = open('files/26-102.txt', 'r')
r = 4
sp = []

for i in f:
    sp.append(i.split())

for i in range(len(sp)):
    sp[i][0] = int(sp[i][0])

sp.sort(reverse=True)

c = 0
max_cb = 0

while len(sp) != 0:
    cb = 1 #Количество контейнеров в блоке
    c += 1 #Количество блоков
    alpha_size = sp[0][0]
    alpha_color = sp[0][1]
    sp[0] = 0

    for i in range(1, len(sp)):
        if sp[i][0] + r <= alpha_size:
            if sp[i][1] != alpha_color:
                cb += 1
                alpha_size = sp[i][0]
                alpha_color = sp[i][1]
                sp[i] = 0

    max_cb = max(cb, max_cb)

    while 0 in sp:
        sp.remove(0)

print(c, max_cb)

