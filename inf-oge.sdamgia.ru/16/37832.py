n = int(input())
c = 0

for i in range(n):
    a = int(input())
    if a % 4 == 0:
        c += 1

print(c)