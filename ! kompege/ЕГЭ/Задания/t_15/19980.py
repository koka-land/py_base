for p in range(2):
    for q in range(2):
        for a in range(2):
            f = ((not(p)) and (not(q)) and (not(a)))
            print(p, q, a, int(f))
