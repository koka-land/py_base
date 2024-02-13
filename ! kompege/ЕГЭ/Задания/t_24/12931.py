f = open('files/24_12931.txt')

s = f.readline()
search = 'VWXYZ'
max_len = 0

while search in s:
    cc = s.count(search)
    c0 = 0
    for i in range(cc):
        c0 = s.index(search, c0)
        cd = len(search)
        for i in range(1, 5):
            if s[c0 - i] == search[i * -1]:
                cd += 1
            else:
                break
        for i in range(4):
            if s[c0 + len(search) + i] == search[i]:
                cd += 1
            else:
                break
        c0 += 1
        max_len = max(max_len, cd)
    search += 'VWXYZ'


print(max_len)
