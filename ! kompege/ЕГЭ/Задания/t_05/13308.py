mar_r = 0

for n in range(1, 13500):
    r = bin(n)[2:]
    r += r[-1]
    r += str(sum(list(map(int, r))) % 2)
    r = int(r, 2)
    if r < 13500:
        mar_r = max(mar_r, r)

print(mar_r)
