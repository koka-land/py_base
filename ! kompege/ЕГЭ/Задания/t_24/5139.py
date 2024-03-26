s = open('files/24_5139.txt').readline()

#1 способ
ch = 'ABCDEFU'
gl = 'AEU'
sogl = 'BCDF'

for i in ch:
    if i in gl:
        s = s.replace(i, '1')
    else:
        s = s.replace(i, '0')

strr = '010'

while strr in s:
    strr += '010'

print((len(strr) - 3) // 3)

#2 способ
i = 0
count = 0
maxx = 0

while i < len(s):
    if s[i:i + 3] == '010':
        i += 3
        count += 1
        maxx = max(maxx, count)
    else:
        i += 1
        count = 0

print(maxx)
