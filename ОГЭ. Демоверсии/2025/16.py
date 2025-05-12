n = int(input())

temp = 0
day = 0

for i in range(n):
    a = int(input())
    if a > 0:
        day = day + 1
        temp = temp + a

print(temp / day)
print(day)