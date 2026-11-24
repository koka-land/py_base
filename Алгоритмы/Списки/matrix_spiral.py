row_count = int(input())
col_count = int(input())

matrix = [[0] * col_count for _ in range(row_count)]
top, left = 0, 0
bottom, right = row_count - 1, col_count - 1
number = 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top][i] = number
        number += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = number
        number += 1
    right -= 1
    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = number
            number += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = number
            number += 1
        left += 1

for row in matrix:
    for element in row:
        print(f'{element:<4}', end='')
    print()