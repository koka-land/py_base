from itertools import product

mask = [255, 224, 0, 0]
serv = [117, 32, 0, 0]
i1 = 117


for i2, i3, i4 in product(range(0, 256), repeat=3):
    if i2 & mask[1] == serv[1]:
        print(i1,i2,i3,i4)

