s = '7' * 333

while '66' in s or '77777' in s:
    if '66' in s:
        s = s.replace('66', '7', 1)
    else:
        s = s.replace('77777', '676676', 1)

print(6 ** s.count('6') * 7 ** s.count('7'))