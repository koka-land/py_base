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
    station = []
    while len(sp) != 0 and sp[0][0] == i:
        station.append(sp[0][1])
        sp.pop(0)
    station.sort(reverse=True)
    while len(train) != 0 and train[0] == i:
        luckers += 1
        train.pop(0)
    while len(train) != place and len(station) != 0:
        train.append(station[0])
        station.pop(0)
    if len(train) == place:
        full += 1
    train.sort()

print(luckers, full)
