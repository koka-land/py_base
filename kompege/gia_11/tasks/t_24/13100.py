f = open('files/24_13100.txt')

s = f.readline()

len_max = 0

for i in range(len(s)):
    c = 0
    d = 0
    str_now = 0
    for j in range(i, len(s)):
        if s[j] == 'C':
            c += 1
        if s[j] == 'D':
            d += 1
        if c < 3 and d < 3:
            str_now += 1
        else:
            break
    len_max = max(len_max, str_now)

print(len_max)