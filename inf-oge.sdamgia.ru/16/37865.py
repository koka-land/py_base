c = 0

for i in range(8):
    a = int(input())
    if a % 3 == 0 and a % 10 == 4:
        c += 1

print(c)