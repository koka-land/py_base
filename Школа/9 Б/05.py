matrix = []
for y in range(6):
    matrix += [[int(input()) for _ in range(6)]]

print('Before')
for y in matrix:
    print(y)

col = 0
max_left = max_right = 0

for y in range(6):
    for x in range(6):
        if x <= col:
            if max_left < matrix[y][x]:
                left = [y, x]
                max_left = matrix[y][x]
        else:
            if max_right < matrix[y][x]:
                right = [y, x]
                max_right = matrix[y][x]
    col += 1

matrix[left[0]][left[1]] = max_right
matrix[right[0]][right[1]] = max_left

print('After')
for y in matrix:
    print(y)
