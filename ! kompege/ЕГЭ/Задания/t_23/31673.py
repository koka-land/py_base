f = open('files/23_31673.txt')
sp = []

for i in f:
    s = i.split()
    sp.append([int(s[0]), int(s[1]), float(s[2])])
sp.sort()
print(sp)