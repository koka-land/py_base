n = int(input())
max5 = 0

for i in range(n):
    a = int(input())
    if a % 5 == 0 and a > max5:
        max5 = a

print(max5)