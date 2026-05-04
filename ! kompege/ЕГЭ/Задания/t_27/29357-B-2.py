f = open('files/27_B_29357.txt')
cl   = [[], [], []]
cl_c = [[], [], []]
og   = [0, 0, 0]
yc   = [[], [], []]
ans2 = 0

for i in f:
    x, y, par = i.split()
    x, y = float(x), float(y)
    if y < 30:
        n = 0
    elif x < 16:
        n = 1
    else:
        n = 2

    cl[n].append([x, y])
    if par[0] == 'K' and 'III' in par:
        og[n] += 1
    if par[0] == 'G' and par[-1] == 'V' and 'IV' not in par:
        yc[n].append([x, y])

for n in range(3):
    min_s = 10**10
    for star in cl[n]:
        s = 0
        for sub_star in cl[n]:
            s += ((star[0] - sub_star[0])**2 + (star[1] - sub_star[1])**2)**0.5
        if s < min_s:
            min_s = s
            cl_c[n] = star

    for star in yc[n]:
        for sub_star in yc[n]:
            s = ((star[0] - sub_star[0]) ** 2 + (star[1] - sub_star[1]) ** 2) ** 0.5
            if s > ans2:
                ans2 = s


max_og = og.index(max(og))
min_og = og.index(min(og))

ans1 = ((cl_c[max_og][0] - cl_c[min_og][0])**2 + (cl_c[max_og][1] - cl_c[min_og][1])**2)**0.5
print(int(ans1 * 10000))
print(int(ans2 * 10000))
