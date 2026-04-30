sp = [[16, 12],
      [-8, -10],
      [18, 2],
      [5, -5],
      [1, -9],
      [10, 9],
      [-10, -2],
      [14, 1],
      [20, 5]]
for A in range(-100, 100):
    yes = 0
    no = 0
    for i in sp:
        if (i[0] < A) or (i[1] > 8):
            yes += 1
        else:
            no += 1
    if no == 4:
        print(A)
