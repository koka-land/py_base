row_count = int(input())
column_count = int(input())
number = row_count * column_count
table = []

for _ in range(row_count):
    row = [0] * column_count
    table.append(row)

len_number = len(str(number)) + 1

for row in range(row_count):
    if row % 2 == 0:
        for column in range(column_count):
            table[row][column] = number
            number -= 1
    else:
        for column in range(column_count - 1, -1, -1):
            table[row][column] = number
            number -= 1

for row in table:
    for element in row:
        print(f'{element:>{len_number}}', end='')
    print()