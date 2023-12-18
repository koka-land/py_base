a = 5 * 216**165 - 4 * 36**164 + 5 * 666163 - 2 * 6**162 - 161
count = 0

while a > 0:
    if a % 36 > 10:
        count += 1
    a //= 36

print(count)