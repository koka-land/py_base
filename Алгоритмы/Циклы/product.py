from itertools import product
sp = []
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, 3):
    sp.extend(list(product(num, repeat=i)))
print(sp)