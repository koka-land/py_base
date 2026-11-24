row_count = int(input())
column_count = int(input())
number = 1
table = []

for _ in range(row_count):
    row = [0] * column_count
    table.append(row)

for column in range(column_count):
    if column % 2 == 0:
        for row in range(row_count):
            table[row][column] = number
            number += 1
    else:
        for row in range(row_count - 1, -1, -1):
            table[row][column] = number
            number += 1

len_number = len(str(number)) + 1

for row in table:
    for element in row:
        print(f'{element:>{len_number}}', end='')
    print()