ans = 0

for n in range(1350051, 10**10):
    sp = [int(i) for i in sum([[str(x), str(n // x)] for x in range(2, int(n**0.5) + 1) if n % x == 0], []) if i[-2:] == '11' and len(i) > 2]
    if len(sp) != 0:
        ans += 1
        print(n, min(sp))
        if ans == 5:
            break