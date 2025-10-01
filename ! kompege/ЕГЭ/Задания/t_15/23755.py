print('p q a f')
for p in range(2):
    for q in range(2):
        for a in range(2):
            f = (p <= ((q and (not(a))) <= (not(p))))
            print(p, q, a, int(f))
