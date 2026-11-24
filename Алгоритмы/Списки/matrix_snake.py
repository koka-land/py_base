matrix = []

row_count = int(input())
col_count = int(input())
number = 1

for r in range(row_count):
    row = []
    for _ in range(col_count):
        if r % 2 == 0:
            row.append(number)
        else:
            row.insert(0,number)
        number += 1
    matrix.append(row)
len_number = len(str(number)) + 1
for r in matrix:
    for elem in r:
        print(f'{elem:>{len_number}}', end='')
    print()
