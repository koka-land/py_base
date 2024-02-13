s = '7' * 116

while '333' in s or '7777' in s:
    if '333' in s:
        s = s.replace('333', '7', 1)
    else:
        s = s.replace('7777', '3', 1)

print(s)