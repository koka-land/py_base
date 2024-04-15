f = open('files/26.txt')
sp = []
l, p, n = map(int, f.readline().split())

for i in f:
    sp.append(list(map(int, i.split())))

sp.sort()

lot = 0
stavki = []
otvet1 = 0
otvet2 = 0

for i in sp:
    if i[0] == lot:
        stavki.append(i[2])
    else:
        if len(stavki) > 1:
            stavki.sort()
            otvet1 += 1
            otvet2 += stavki[-2]
        lot = i[0]
        stavki = []
        stavki.append(i[2])
if len(stavki) > 1:
    stavki.sort()
    otvet1 += 1
    otvet2 += stavki[-2]

print(otvet1, otvet2)