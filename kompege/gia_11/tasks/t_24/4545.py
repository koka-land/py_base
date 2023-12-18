f = open('files/24_4545.txt')

s = f.readline()
l = 0
max_l = 0
i = 0

while i <= len(s) - 3:
    if s[i:i+3] == 'XYZ' or s[i:i+3] == 'ZYX':
        l += 1
        i += 3
    else:
        max_l = max(max_l, l)
        l = 0
        i += 1

print(max_l)

#2 способ

s = s.replace('ZYX', '3')
s = s.replace('XYZ', '3')
sp = '3'
while sp in s:
    sp += '3'

print(len(sp) - 1)