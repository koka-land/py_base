end = 0

for ss in range(7, 17):
    for y in range(0, ss):
        for x in range(0, ss):
            for z in range(0, ss):
                a = y * ss**2 + 4 * ss + y
                b = y * ss**2 + 6 * ss + 5
                c = x * ss**3 + z * ss**2 + 2*ss + 3
                if a + b == c:
                    print(int(str(x) + str(y) + str(z), ss))
                    end == 1
                    break
            if end == 1:
                break
        if end == 1:
            break
    if end == 1:
        break