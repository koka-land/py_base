s = 0
for n in range(5, 32, 2):
    s += n / (n + 3)

print(round(s, 3))