c = 0

while True:
    a = int(input())
    if a == 0:
        break
    if abs(a) % 2 == 0 and abs(a) % 7 == 0:
        c += 1

print(c)