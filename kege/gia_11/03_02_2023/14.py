a = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023
count = 0

while a > 0:
    if a % 6 == 0:
         count += 1
    a //= 6

print(count)