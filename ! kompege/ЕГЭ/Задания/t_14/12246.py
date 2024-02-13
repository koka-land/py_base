a = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338

count = 0

while a > 0:
    if a % 9 != 0:
        count += 1
    a = a // 9

print(count)