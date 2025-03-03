a = 50
с = 0

while a != 0:
    a = int(input())
    if a % 7 == 0 and a != 0 and a % 2 == 0:
        с += 1

print(с)