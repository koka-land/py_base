import string

s = (string.digits + string.ascii_uppercase)[:34]

for x in s:
    a = int('GP45' + x + '2', 34) + int('P7' + x, 34) * int(x + 'AI98', 34)
    if a % 13 == 0:
        print(x, int(x, 34), a // 13)