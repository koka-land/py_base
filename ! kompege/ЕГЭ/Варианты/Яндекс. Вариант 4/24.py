s = open('files/24.txt').readline()
num = '0123456789'
c = ''
maxx = 0
for i in s:
    if i in num:
        c += i
        if int(c) % 2 == 0:
            maxx = max(maxx, int(c))
    else:
        c = ''

print(maxx)