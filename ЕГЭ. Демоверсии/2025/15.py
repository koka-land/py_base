for p in range(2):
    for q in range(2):
        for a in range(2):
            print(p, q, a, (p <= ((q and (not(a))) <= (not(p)))))