f = open('files/26_11921.txt')
robots = []
bat = []

robot_count = int(f.readline())
for i in range(robot_count):
    robots.append(int(f.readline()))
bat_count = int(f.readline())
for i in f:
    bat.append(list(map(int, i.split())))

max_prise = 0
prise = 0

for i in robots:
    min_prise = 10**10
    for j in bat:
        if j[0] >= i:
            min_prise = min(min_prise, j[1])
    prise += min_prise
    max_prise = max(min_prise, max_prise)

print(prise, max_prise)