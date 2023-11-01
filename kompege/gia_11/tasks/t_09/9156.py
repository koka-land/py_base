f = open('files/09_9156.csv')
count = 0

for i in f:
    sp = list(map(int, i.split(';')))
    if (max(sp) + min(sp)) % 3 == 0:
        if (abs(sp[0] - sp[1]) == abs(sp[2] - sp[3])) or (abs(sp[0] - sp[2]) == abs(sp[1] - sp[3])) or (abs(sp[0] - sp[3]) == abs(sp[1] - sp[2])):
            count += 1

print(count)

