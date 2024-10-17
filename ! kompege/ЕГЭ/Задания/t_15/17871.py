print('P Q A F')
for P in range(2):
    for Q in range(2):
        for A in range(2):
            F = P <= ((Q and not(A)) <= (not(P)))
            if F == False:
                print(P, Q, A, F)