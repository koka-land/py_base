print('a p q f')
for a in range(2):
    for p in range(2):
        for q in range(2):
            f = (not(q <= (((not a) and p) <= (not q))))
            print(a, p, q, int(f))