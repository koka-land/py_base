from itertools import product

f = open('files/24_8567.txt')

s = f.readline()
list_b = []

for i1, i2, i3 in product('ABCD', repeat=3):
    list_b.append(i1 + i2 + i3)

max_count = 0
stroka = ''

for i in range(len(s)):
    if s[i] not in 'ABCD':
        stroka += s[i]
    else:
        if s[i:i+3] in list_b:
            stroka += s[i:i+2]
            max_count = max(max_count, len(stroka))
            stroka = ''
        else:
            stroka += s[i]

max_count = max(max_count, len(stroka))

print(max_count)
