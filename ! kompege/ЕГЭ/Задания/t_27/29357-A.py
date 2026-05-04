fa = open('files/27_A_29357.txt')
sp_a = [[], []]
sp_a_red = []
stars = [[], []]
for i in fa:
    sp = i.split()
    if sp[2][0] == 'M' and sp[2][-3:] == 'III':
        sp_a_red.append([float(sp[0]), float(sp[1])])
    if float(sp[1]) < 15:
        sp_a[0].append([float(sp[0]), float(sp[1])])
    else:
        sp_a[1].append([float(sp[0]), float(sp[1])])

for i in range(2):
    min_sr = 10**10
    for star in sp_a[i]:
        sr = 0
        for j in sp_a[i]:
            sr += ((j[0] - star[0])**2 + (j[1] - star[1])**2)**0.5
        if sr < min_sr:
            stars[i] = star
if len(sp_a[0]) < len(sp_a[1]):
    len_a = 0
else:
    len_a = 1

min_red = 10**10
red_x = 0
red_y = 0
for i in sp_a_red:
    ras = ((stars[len_a][0] - i[0])**2 + (stars[len_a][1] - i[1])**2)**0.5
    if ras < min_red:
        min_red = ras
        red_x = i[0]
        red_y = i[1]

print(int(red_x * 10000), int(red_y * 10000))

