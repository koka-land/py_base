s = '1' * 169

while '13' in s or '14' in s or '11' in s:
    if '13' in s:
        s = s.replace('13', '33', 1)
    elif '14' in s:
        s = s.replace('14', '44', 1)
    else:
        s = s.replace('11', '43', 1)

print(s.count('4'))
