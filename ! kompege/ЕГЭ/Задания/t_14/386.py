def p(x, ss):
    sum = 0
    while x > 0:
        sum += x % ss
        x //= ss
    return sum

for i in range(2, 100):
    if p(i**25 - 2 * i**13 + 10, i) == 75:
        print(i)
        break