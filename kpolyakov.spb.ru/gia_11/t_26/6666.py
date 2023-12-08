'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6666
'''

f = open('files/26-126.txt')

point, place, people = map(int, f.readline().split())

sp = []
full = 0
luckers = 0

for i in f:
    sp.append(list(map(int, i.split())))
sp.sort()

train = []

for i in range(1, point + 1):
    if len(train) == place:
        full += 1
    train.sort()
    station = []
    if len(sp) != 0:
        while sp[0][0] == i:
            station.append(sp[0][1])
            sp.pop(0)
            if len(sp) == 0:
                break
    station.sort(reverse=True)
    if len(train) != 0:
        while train[0] == i:
            luckers += 1
            train.pop(0)
            if len(train) == 0:
                break
    while len(train) <= place or len(station) != 0:
        if len(station) == 0:
            break
        else:
            if len(train) != place:
                train.append(station[0])
                station.pop(0)
            else:
                break

print(luckers, full)

