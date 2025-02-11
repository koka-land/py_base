bombs = [[2, 3], [3, 5], [4, 8]]
print(bombs)
a = int(input())
b = int(input())

c = 0
for x in range(a - 1, a + 2):
    for y in range(b - 1, b + 2):
        if [x, y] in bombs:
            c += 1
print(c)