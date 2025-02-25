n = int(input())
s = 0

for i in range(n):
    a = int(input())
    if a % 6 == 0:
        s += a

print(s)