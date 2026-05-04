f = open('files/27_B_29357.txt')
sp = [[], [], []]
og = [0, 0, 0]
yc = [[], [], []]
stars = [[], [], []]

for i in f:
    sp_p = i.split()
    if float(sp_p[1]) < 30:
        sp[0].append([float(sp_p[0]), float(sp_p[1])])
        if sp_p[2][0] == 'K' and sp_p[2][-3:] == 'III':
            og[0] += 1
        if sp_p[2][0] == 'G' and sp_p[2][-1] == 'V' and sp_p[2][-2] != 'I':
            yc[0].append([float(sp_p[0]), float(sp_p[1])])
    elif float(sp_p[0]) < 16:
        sp[1].append([float(sp_p[0]), float(sp_p[1])])
        if sp_p[2][0] == 'K' and sp_p[2][-3:] == 'III':
            og[1] += 1
        if sp_p[2][0] == 'G' and sp_p[2][-1] == 'V' and sp_p[2][-2] != 'I':
            yc[1].append([float(sp_p[0]), float(sp_p[1])])
    else:
        sp[2].append([float(sp_p[0]), float(sp_p[1])])
        if sp_p[2][0] == 'K' and sp_p[2][-3:] == 'III':
            og[2] += 1
        if sp_p[2][0] == 'G' and sp_p[2][-1] == 'V' and sp_p[2][-2] != 'I':
            yc[2].append([float(sp_p[0]), float(sp_p[1])])

for i in range(3):
    min_sr = 10**10
    for star in sp[i]:
        sr = 0
        for j in sp[i]:
            sr += ((j[0] - star[0])**2 + (j[1] - star[1])**2)**0.5
        if sr < min_sr:
            min_sr = sr
            stars[i] = star

max_sr = 0

for i in range(3):
    for star in yc[i]:
        sr = 0
        for j in yc[i]:
            sr = ((j[0] - star[0])**2 + (j[1] - star[1])**2)**0.5
            if sr > max_sr:
                max_sr = sr

max_ = og.index(max(og))
min_ = og.index(min(og))
ans1 = ((stars[min_][0] - stars[max_][0])**2 + (stars[max_][1] - stars[min_][1])**2)**0.5
print(int(ans1 * 10000))
print(int(max_sr * 10000))



