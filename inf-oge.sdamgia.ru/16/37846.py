ans = 0
a = 1
while a != 0:
    a = int(input())
    if a != 0:
        if a % 6 == 0 and a % 10 == 4:
            ans = ans + a
print(ans)
