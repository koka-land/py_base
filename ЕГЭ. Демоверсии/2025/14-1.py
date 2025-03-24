import string
s = string.digits + string.ascii_uppercase[:9]

ans = [(int(f'98897{i}21', 19) + int(f'2{i}923', 19)) // 18 for i in s if (int(f'98897{i}21', 19) + int(f'2{i}923', 19)) % 18 == 0]

print(max(ans))
