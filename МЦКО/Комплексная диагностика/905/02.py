from itertools import product

print('w x y z')
for w, x, y, z in product([0, 1], repeat=4):
    f = (w == z) or not(y <= w) or not(x)
    if f == 0:
        print(w, x, y, z)