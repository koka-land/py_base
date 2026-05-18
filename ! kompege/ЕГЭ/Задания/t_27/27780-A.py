f_a = open('files/27A_27780.txt')

def distany(s1, s2):
    d = ((s2[0] - s1[0])**2 + (s2[1] - s1[1])**2)**0.5
    return d

def find_center(x):
    min_s = 10**10
    centr = []
    for star in x:
        s = sum(distany(star, j) for j in x)
        if s < min_s:
            min_s = min(min_s, s)
            centr = star
    return centr

cl_a = [[], []]

for i in f_a:
    x, y = map(float, i.split())
    if y < 15:
        cl_a[0].append([x, y])
    else:
        cl_a[1].append([x, y])

#A1
print(max(len(i) for i in cl_a))
#A2
centr_a = [find_center(i) for i in cl_a]
print(int(sum(distany(i, [1.0, 1.5]) for i in centr_a) * 10000))


