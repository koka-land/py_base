a = 625**90 + 125**120 - 5 * 25
summ = 0

while a > 0:
    if (a % 25) % 2 == 0:
        summ += a % 25
    a //= 25

print(summ)