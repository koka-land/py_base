f = open('files/24.txt', 'r')
s = f.readlines()
sym = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str = ''

for i in s:
    str = str + i + ' '
print(str.count(' '))

for i in sym:
    search = i
    while search in str:
        search = search + i
    print(search)
    search = search[:-1]
    print(search)
