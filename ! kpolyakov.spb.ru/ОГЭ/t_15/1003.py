a = 5
s = 0

while a != 0:
    a = int(input())
    if a % 7 == 0 and a % 10 == 2:
        s += a

print(s)