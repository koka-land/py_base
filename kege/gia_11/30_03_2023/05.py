max = 0

for n in range(1, 8):
    if n % 2 == 0:
        n = bin(n)[2::] + '10'
    else:
        n = '1' + bin(n)[2::] + '01'
    r = int(n, 2)
    if r > max:
        max = r

print(max)
