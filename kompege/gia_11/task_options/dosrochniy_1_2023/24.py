f = open('files/24_7600.txt')
s = f.readline()
er = ['QR', 'RQ', 'SQ', 'QS', 'RS', 'SR', 'QQ', 'RR', 'SS']

count = 1
max_count = 0
for i in range(len(s) - 1):
    if s[i:i+2] in er:
        max_count = max(max_count, count)
        count = 1
    else:
        count += 1

print(max_count)
