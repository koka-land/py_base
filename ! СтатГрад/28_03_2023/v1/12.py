def prime(a):
    f = 0
    for i in range(2, int(a ** (1 / 2)) + 1):
        if a % i == 0:
            f = 1
            break
    if f == 0:
        return 0
    else:
        return 1

end = 0

for a1 in range(69, 1500):
    sum = 0
    s = '0' + '1' * a1 + '2' * a1 + '0'
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    for i in s:
        sum += int(i)
    if prime(sum) == 0:
        print(a1)
        break
