import string
x = (string.digits + string.ascii_uppercase)[:25]
ans = []

for c in x:
    a = int('a4' + c + '7f2', 25) + int('n' + c + 'g5' + c + 'h', 25) + int('74' + c + 'm26', 25)
    if a % 24 == 0:
        ans.append(a // 24)

print(max(ans))